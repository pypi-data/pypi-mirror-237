from typing import NamedTuple, List

from unipipeline.errors import UniError
from unipipeline.modules.uni import Uni


class DataStreamStats(NamedTuple):
    messages_count: int
    queue_name: str
    error_queue: bool


def get_data_streams_stats(uni: Uni) -> List[DataStreamStats]:
    stats = []
    for wd in uni.config.workers.values():
        try:
            broker = uni._mediator.get_broker(wd.broker.name)
            success_messages_count = broker.get_topic_approximate_messages_count(wd.topic)
            error_messages_count = broker.get_topic_approximate_messages_count(wd.error_topic)
            stats.append(DataStreamStats(
                messages_count=success_messages_count,
                queue_name=wd.topic,
                error_queue=False,
            ))
            stats.append(DataStreamStats(
                messages_count=error_messages_count,
                queue_name=wd.error_topic,
                error_queue=True,
            ))
        except UniError:
            pass

    return stats
