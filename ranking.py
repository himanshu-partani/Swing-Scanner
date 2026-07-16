def sort_results(results):
    """
    Sort stocks by overall score (highest first).
    """
    return sorted(
        results,
        key=lambda stock: stock["score"],
        reverse=True,
    )