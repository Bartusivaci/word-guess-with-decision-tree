"""
    To use this implementation, you simply have to implement `agent_function` such that it returns a legal action.
    You can then let your agent compete on the server by calling
        python3 example.py path/to/your/config.json
    
    You can interrupt the script at any time.
    The server will remember the actions you have sent.

    Note:
        By default the client bundles multiple requests for efficiency.
        This can complicate debugging.
        You can disable it by setting `parallel_runs=False` in the last line.
"""


def agent_function(request_data, request_info):
    # TODO: Implement this function in a better way.
    # The request_data contains all the relevant information (map, history, ...).
    # You can ignore request_info.
    print('I got the following request:')
    print(request_data)



    return 'APPLE'      # most of the time this will be wrong


if __name__ == '__main__':
    import sys, logging
    from client import run

    # You can set the logging level to logging.WARNING or logging.ERROR for less output.
    logging.basicConfig(level=logging.INFO)

    run(
        agent_function=agent_function,
        agent_config_file=sys.argv[1],
        parallel_runs=True,     # Set it to False for debugging.
        run_limit=1000,         # Stop after 1000 runs. Set to 1 for debugging.
    )

