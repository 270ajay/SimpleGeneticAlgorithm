

def logger(logging):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(message)s',
                        #datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename='../output/gaOptimization.log', filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # console.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s %(process)d %(message)s'))
    logging.getLogger().addHandler(console)