import wikipedia

def search(query, num_returned=10):
    search_params = {
        'list': 'search',
        'srprop': '',
        'srlimit': num_returned,
        'limit': num_returned,
        'srsearch': query,
        'srwhat': 'text',
        'srprop': 'snippet|sectionsnippet',
    }

    raw_results = wikipedia.wikipedia._wiki_request(search_params)

    if 'error' in raw_results:
        if raw_results['error']['info'] in ('HTTP request timed out.', 'Pool queue is full'):
            raise ValueError("HTTP timeout")
        else:
            raise ValueError(raw_results['error']['info'])

    return raw_results['query']['search']
