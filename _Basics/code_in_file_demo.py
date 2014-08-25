

def get_globals_without_hidden():
    """
    extracts the context without hidden (aka __*) fields
    """
    ctx = globals()
    ret = []
    for key, value in ctx.iteritems():
        if not key.startswith("__"):
            ret.append( "%-10s = %s" % (key, value,) )
    return "\n".join(ret)


logger.info('-'*80)
logger.info("Hi, I'm in a file.")
logger.info("my globals are this: [%s]", (get_globals_without_hidden(),))
logger.info('-'*80)

payload = "Value from file execution."
    
