# alphabet-thief
"Hi, I am an alphabet thief. I steal every Latin alphabet from A to Z."

## Requirements
- Python >= 3.7

## Installation
```
pip install alphabet_thief
```

## Usage
```python
import alphabet_thief

text = 'Hello, how are you?'
result = alphabet_thief.steal(text)
print(f'"{}"')
```

```
"     ,            ?"
```

```python
text = 'Hello, how are you?'
result = alphabet_thief.replace(text, 'a')
print(f'"{}"')
```

```
"aaaaa, aaa aaa aaa?"
```

```python
text = 'Trời mưa thì phải ở nhà.'
result = alphabet_thief.steal(text)
print(f'"{}"')
```

```
"   ̛̀    ̛     ̀    ̉   ̛̉    ̀."
```

```python
text = 'Trời mưa thì phải ở nhà.'
result = alphabet_thief.replace(text, 'a')
print(f'"{}"')
```

```
"aaà̛a aa̛a aaà aaảa ả̛ aaà."
```
