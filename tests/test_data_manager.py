from exp_check.data_manager import DataManager

def test_data_manager():
    '''Driver test code'''
    dm = DataManager("./junk.json")
    print("--- init")
    print(dm.to_string())
    
    print("--- delete 'A cool can of beans'")
    msg = dm.delete_entry("A cool can of beans")
    assert msg is not None, msg

    print(dm.to_string())
    
    print("--- delete 'goo'")
    msg = dm.delete_entry("goo")
    assert msg is not None, msg


    print(dm.to_string())

    print("--- add goo 181202") 
    msg = dm.add_entry("goo", "181202")
    assert msg is None, msg

   
    print(dm.to_string())
    
    print("--- add y nice can of beans 181201")
    msg = dm.add_entry("y nice can of beans", "181201")
    assert msg is None, msg

    
    print(dm.to_string())
    print(dm.get_metadata())
    print(dm.get_keylist(),'\n')
    db = dm.get_database(dm.get_keylist())
    for i in db:
        print(i)
    
    print("\n")
    db = dm.get_database(dm.get_keylist(), sort_key='name')
    for i in db:
        print(i)
    
    print("\n")
    db = dm.get_database(dm.get_keylist(), sort_key='date added')
    for i in db:
        print(i)
    
    print("\n")
    db = dm.get_database(dm.get_keylist(), sort_key='expiration date')
    for i in db:
        print(i)
    
    assert False
