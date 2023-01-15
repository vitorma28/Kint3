text = input('Digite o texto:\n\n')
code = int(input('\n[1] Criptografar\n[2] Descriptografar\n\n> '))
print()
key = input(
  'Insira a chave(Menor ou igual a quantidade de caracteres da mensagem): ')

vocab = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z', 'Ç', 'ç', 'Á', 'Â', 'Ã', 'À', 'É', 'Ê',
  'Í', 'Î', 'Ó', 'Õ', 'Ô', 'Ú', 'Û', 'á', 'â', 'ã', 'à', 'é', 'ê', 'í', 'î',
  'ó', 'ô', 'ú', 'û', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
  '@', '#', '$', '%', '&', '*', '(', ')', '-', '=', '+', '§', '[', '{', ']',
  '}', ',', '.', ';', ':', '/', '?', '\\', '|', '\'', '"', ' '
]


def encrypt(char: str, key: str) -> str:
  n = 0
  for i in range(len(vocab)):
    if key == vocab[i]:
      k = i
  for i in range(len(vocab)):
    if char == vocab[i]:
      n = i
  r = n - k
  while r > len(vocab) - 1:
    r -= len(vocab)
  while r < (len(vocab) * -1) + 1:
    r += len(vocab)
  return vocab[r]


def decrypt(char: str, key: str) -> str:
  r = 0
  for i in range(len(vocab)):
    if key == vocab[i]:
      k = i
  for i in range(len(vocab)):
    if char == vocab[i]:
      r = i
  n = r + k
  while n > len(vocab) - 1:
    n -= len(vocab)
  while n < (len(vocab) * -1) + 1:
    n += len(vocab)
  return vocab[n]


print('\nResultado:\n')
count = 0
turns = len(key)
if turns > 64:
  turns = 64
if code == 1:
  txt = list(text)
  for i in range(turns):
    index = 0
    while index < len(txt):
      if count >= len(key):
        count = 0
      txt[index] = encrypt(txt[index], key[count])
      count += 1
      index += 1
  txt = ''.join(txt)
  print(txt)
else:
  txt = list(text)
  for i in range(turns):
    index = 0
    while index < len(txt):
      if count >= len(key):
        count = 0
      txt[index] = decrypt(txt[index], key[count])
      count += 1
      index += 1
  txt = ''.join(txt)
  print(txt)

print('\n\n')
