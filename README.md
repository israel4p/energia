# Energia

# Criar imagem

```sh
build . -t energia:latest
```
## Subindo a imagem criada

```sh
docker run -d \
  --name energia-app \
  -v /volume/energia-db:/app/database \
  -m 128M \
  --restart always \
  energia:latest
```
