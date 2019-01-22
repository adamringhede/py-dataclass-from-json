# py-dataclass-from-json

Generate code for python data classes using example JSON. 


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