from alive_progress import alive_bar


def spinner(show_progress: bool = True):
    return alive_bar(
        0,
        bar=None,
        monitor=False,
        stats=False,
        elapsed=False,
        receipt=False,
        enrich_print=False,
        disable=not show_progress,
    )
