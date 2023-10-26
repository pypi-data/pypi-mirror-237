/* Get the the test result of the last 14 days */
with

test_results_last_14_days as (
    select  *
            ,concat(
                coalesce(nullif(split(table_name,'.')[2],''),'-'),'|',
                coalesce(nullif(column_name,''),'-'),'|',
                coalesce(nullif(split(ref_table,'.')[2],''),'-'),'|',
                coalesce(nullif(ref_column,''),'-'),'|',
                test_unique_id
            ) as test_id
            ,case
                --when datediff(day, check_timestamp, sysdate()) >=3 then 'deprecated'
                when no_of_records_failed > 0 and severity = 'error' then 'failed'
                when no_of_records_failed > 0 and severity = 'warn' then 'warn'
                else 'pass'
            end as test_status

    from    @database.@schema.dq_issue_log
    where   true
        --exclude dq-tools models
        and table_name not ilike '%bi_column_analysis%'
        and table_name not ilike '%bi_dq_metrics%'
        and table_name not ilike '%test_coverage%'
        --time limited to the last 14 days
        and check_timestamp > dateadd(day, -14, sysdate())
),

latest_status as (

    select  test_id
            ,test_status
            ,check_timestamp
            ,no_of_records_scanned
            ,no_of_records_failed
            ,dq_issue_type
            ,kpi_category

    from    test_results_last_14_days

    qualify row_number() over (partition by test_id order by check_timestamp desc) = 1

),

prev_statuses as (

    select  test_id
            ,array_agg(test_status) within group (order by check_timestamp desc) as prev_statuses
            ,array_agg(check_timestamp) within group (order by check_timestamp desc) as prev_check_timestamps
            ,array_agg(no_of_records_scanned) within group (order by check_timestamp desc) as prev_no_of_records_scanned
            ,array_agg(no_of_records_failed) within group (order by check_timestamp desc) as prev_no_of_records_failed

    from    test_results_last_14_days

    group by test_id

)

select      '[dq-tools] ' || test_id as jira_ticket_summary
            ,latest_status.test_id
            ,latest_status.test_status
            ,latest_status.check_timestamp
            ,latest_status.no_of_records_scanned
            ,latest_status.no_of_records_failed
            ,latest_status.dq_issue_type
            ,latest_status.kpi_category
            ,prev_statuses.prev_statuses
            ,prev_statuses.prev_check_timestamps
            ,prev_statuses.prev_no_of_records_scanned
            ,prev_statuses.prev_no_of_records_failed

from        latest_status
left join   prev_statuses using (test_id)
