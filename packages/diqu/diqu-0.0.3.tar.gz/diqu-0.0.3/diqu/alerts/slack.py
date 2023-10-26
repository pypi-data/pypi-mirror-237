import os
import ssl
import string
import uuid

import certifi
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data, limit: int = 3) -> ResultCode:
    slack = Slack()
    template_sum = string.Template(
        "🧵 *Summary on $date:*\n\n"
        "  • ❗ $error_count error(s)\n"
        "  • 👀 $warn_count warning(s)\n"
        "  • ✅ $pass_count pass(es)\n"
        "  • ✅ $deperecated_count deprecation(s)"
    )
    template_incident = string.Template("• $index $status: $incident\n")

    summary = template_sum.substitute(
        date=data.iloc[0, 3],  # CHECK_TIMESTAMP
        error_count=data[data["TEST_STATUS"] == "failed"].shape[0],
        warn_count=data[data["TEST_STATUS"] == "warn"].shape[0],
        pass_count=data[data["TEST_STATUS"] == "pass"].shape[0],
        deperecated_count=data[data["TEST_STATUS"] == "deprecated"].shape[0],
    )

    incidents = ""
    incident_data = data[data["TEST_STATUS"] != "pass"].head(limit)
    for i in range(len(incident_data)):
        status = data.iloc[0, 2]
        incidents += template_incident.substitute(
            index=i + 1,
            status="🔴" if status == "failed" else "🟡",
            incident=data.iloc[0, 0],  # JIRA_TICKET_SUMMARY
        )

    r = slack.post_message(
        blocks=[
            {"type": "section", "text": {"type": "mrkdwn", "text": summary}},
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"👉 *Top {limit} Issues*:\n\n{incidents}",
                },
            },
        ]
    )
    logger.info("✅ Done > Slack")
    return r


class Slack:
    def __init__(self) -> None:
        self.client = WebClient(
            token=os.environ.get("SLACK_TOKEN"),
            ssl=ssl.create_default_context(cafile=certifi.where()),
        )
        self.channel = os.environ.get("SLACK_CHANNEL")
        self.channel_id = self.find_channel_id(self.channel)

    def post_message(self, text=None, blocks=[]):
        """Send Slack message"""
        if not self.channel_id:
            return ResultCode.FAILED

        logger.info(f"Targetted channel: #{self.channel}[{self.channel_id}]")
        sent_blocks = (
            blocks
            if len(blocks) > 0
            else [{"type": "section", "text": {"type": "mrkdwn", "text": text}}]
        )

        message_id = f"mid: #{str(uuid.uuid4()).lower()}"
        sent_blocks.extend(
            [
                {"type": "divider"},
                {
                    "type": "context",
                    "elements": [
                        {"type": "plain_text", "text": message_id, "emoji": True}
                    ],
                },
            ]
        )

        try:
            _ = self.client.chat_postMessage(
                channel=self.channel_id,
                blocks=sent_blocks,
                text=f"{sent_blocks}{message_id}",
                unfurl_links=False,
                unfurl_media=False,
            )
        except SlackApiError as e:
            logger.error(f"Got an error: {e.response['error']}")
            return ResultCode.FAILED

        return ResultCode.SUCCEEDED

    def find_channel_id(self, name: str):
        """Find Slack channel ID by name"""
        try:
            for result in self.client.conversations_list():
                for channel in result["channels"]:
                    if channel["name"] == name:
                        return channel["id"]
        except SlackApiError as e:
            logger.error(str(e))
            return None
