#add import
import question_d

value = int(input('\nPlease enter your property value: '))

assesment_value = question_d.get_assesment_value(value)
tax = question_d.get_tax_assessed(assesment_value)

print('\nYour taxable property value is ' + str(assesment_value) + ', and your property tax is ' + str(tax) + '!\n')