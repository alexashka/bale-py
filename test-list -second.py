
# coding: utf-8

def _all_first_item_to_upper_and_remove_spaces(sentence):
    """ ...
    Args:
    
    Returns:
    """
    # 
    result_string = ''
    space_was = False
    for at in sentence:
        if at != ' ':
            if space_was:
                result_string += at.upper()
                space_was = False
            else:
                result_string += at
        else:
            space_was = True
    #return result_string
    for at in sentence:
     #   at.incert (0, 'const uint16 k')
   # print at   
        at = 'const uint16 k'+at 
    return result_string    

def run():
    test_list = ['Asd dfgdf', 
                 'Dfgghf hgghg',
                 'Lkkkff kfgh']
    for it in test_list:
        print _all_first_item_to_upper_and_remove_spaces(it)
        
        #print it
        #print it.split(' ')
    
if __name__ == '__main__':
   run()

        
    