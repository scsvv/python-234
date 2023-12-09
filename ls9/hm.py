sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

if "city" in sample_dict:
    sample_dict["location"] = sample_dict.pop("city")
else:
    sample_dict["location"] = "N/A"
