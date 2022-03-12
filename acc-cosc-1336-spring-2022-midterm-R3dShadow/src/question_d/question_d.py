#write functions here, don't add input('') statements here!
def get_assesment_value(value):
    assesValue = (value * .6)
    return assesValue

def get_tax_assessed(assesValue):
    return round((assesValue * .0072), 2)