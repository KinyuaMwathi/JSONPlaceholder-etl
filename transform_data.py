def transform_data(data):
    
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids="extract_data")

    transformed_data = []

    for record in data:
        transformed_record = {
            'id': record['id'],
            'name': record['name'],
            'username': record['username'],
            'email': record['email'],
            'address': record['address']['street'] + ', ' + record['address']['city'] + ', ' + record['address']['zipcode']
        }
        transformed_data.append(transformed_record)

    return transformed_data