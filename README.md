# Django Image Serveless

Nesse repositorio tem um pequeno projeto para criar imagens estaticas, para uso em sites
podendo servir como um loren-pixel para uma rede local, sem necessidade de internet


usando o comando :
```shell
python image_serveless.py runserver 0.0.0.0:8883
```

> Usar sempre uma porta diferente para que não conflite com seus otros projetos django, e para ser possivel usar em outros projetos na rede aberto permitindo que outras pessoas usem o seu PC para gerar as imagens 

para usar as imagen geradas em outro projeto use da seguinte forma

```html
<img src="http://[ip]/image/[altura]/[largura]" alt="imagem gerada localmente">
```

#### Exemplo de uso
Uma imagem no seu proprio computador com as dimenções de 800x600
```html
<img src="http://127.0.0.1:8883/image/600/800" alt="imagem gerada localmente">
```





