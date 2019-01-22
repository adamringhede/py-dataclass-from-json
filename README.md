# py-dataclass-from-json

Generate code for python data classes using example JSON. 

This is useful when using a tool to decode json data to objects like
https://pypi.org/project/dataclasses-json/


### Example

Running the below command..
```
python fromjson.py Person <<< '{"name": "Adam"}'
```
... will produce the following output.
````python
@dataclass
class Person():
    name: str



````
