# PDI

**O que é Thresholding?**

Thresholding, ou limiarização, é um tipo de segmentação de imagem que envolve a conversão de uma imagem em escala de cinza para uma imagem binária. Neste processo, escolhe-se um valor de limiar (threshold). Todos os pixels da imagem que têm valores abaixo desse limiar são normalmente definidos como pretos (ou 0), e todos os pixels com valores iguais ou acima do limiar são definidos como brancos (ou 255, no caso de imagens de 8 bits).

**Funcionamento do cv2.threshold**

A função `cv2.threshold` em Python funciona da seguinte forma:

```python
retval, thresholded_image = cv2.threshold(src, thresh, maxval, type)
```

- `src`: Imagem de entrada, que deve estar em escala de cinza.
- `thresh`: O valor do limiar. Pixels com intensidade menor que `thresh` são transformados de acordo com o tipo de thresholding aplicado.
- `maxval`: O valor a ser dado se o pixel tiver intensidade maior ou igual a `thresh`.
- `type`: O tipo de limiarização a ser aplicado. Há várias opções, como:
  - `cv2.THRESH_BINARY`: Os pixels acima do limiar são definidos como `maxval`, e os outros como 0.
  - `cv2.THRESH_BINARY_INV`: Inverte o `THRESH_BINARY`, definindo pixels abaixo do limiar como `maxval`.
  - `cv2.THRESH_TRUNC`: Pixels acima do limiar são definidos como o valor do limiar, o restante permanece inalterado.
  - `cv2.THRESH_TOZERO`: Pixels abaixo do limiar são definidos como 0, o restante permanece inalterado.
  - `cv2.THRESH_TOZERO_INV`: Inverte o `THRESH_TOZERO`.

- `retval`: É o valor do limiar utilizado, que pode ser útil em alguns contextos.
- `thresholded_image`: É a imagem resultante após a aplicação do threshold.

---

A função `cv2.morphologyEx` do OpenCV é uma ferramenta versátil para realizar operações morfológicas avançadas em imagens. A morfologia é uma ampla classe de operações de processamento de imagem que processam imagens com base em formas. Essas operações são aplicadas a imagens binárias, geralmente após a limiarização, e são úteis para remover ruído, separar ou fundir objetos na imagem, e outras tarefas que dependem da forma dos objetos.

**Funcionamento do cv2.morphologyEx**

A função `cv2.morphologyEx` funciona da seguinte maneira:

```python
output_image = cv2.morphologyEx(src, op, kernel, anchor, iterations, borderType, borderValue)
```

- `src`: A imagem de origem.
- `op`: O tipo de operação morfológica a ser realizada. Alguns exemplos comuns incluem:
  - `cv2.MORPH_OPEN`: Abertura. Útil para remover pequenos objetos do primeiro plano (por exemplo, pequenos pontos brancos em uma imagem binária).
  - `cv2.MORPH_CLOSE`: Fechamento. Bom para fechar pequenos buracos no primeiro plano ou pequenos pontos pretos no objeto.
  - `cv2.MORPH_GRADIENT`: Gradiente morfológico. Útil para encontrar os contornos dos objetos.
  - `cv2.MORPH_TOPHAT`: Transformação "Top Hat". Isso destaca os elementos menores da imagem.
  - `cv2.MORPH_BLACKHAT`: Transformação "Black Hat". Útil para destacar pequenos elementos escuros em um fundo claro.
- `kernel`: O elemento estruturante usado para a operação. É uma matriz que decide a natureza da operação. Um kernel comum é uma matriz quadrada de uns.
- `anchor`, `iterations`, `borderType`, `borderValue`: São parâmetros adicionais que especificam a posição do âncora do kernel, o número de vezes que a operação é aplicada, o tipo de borda a ser usada e o valor da borda, respectivamente.

---

**O que é Dilatação?**

A dilatação é uma operação que "cresce" ou "engrossa" os objetos em uma imagem. É particularmente útil para:
- Aumentar o tamanho de objetos em primeiro plano (geralmente brancos em uma imagem binária).
- Conectar áreas separadas.
- Preencher buracos pequenos em objetos.
- Suavizar os contornos dos objetos.

A operação de dilatação funciona considerando o elemento estruturante (ou kernel) e um pixel de âncora. O kernel é deslizado sobre a imagem (como um filtro) e para cada posição do kernel, se pelo menos um pixel sob o kernel é "1", o pixel na posição do âncora é ajustado para "1" (para imagens binárias) ou para o maior valor sob o kernel (para imagens em tons de cinza).

**Funcionamento do cv2.dilate**

A função `cv2.dilate` funciona da seguinte maneira:

```python
dilated_image = cv2.dilate(src, kernel, anchor, iterations, borderType, borderValue)
```

- `src`: Imagem de origem.
- `kernel`: O elemento estruturante utilizado para dilatação. Se nenhum kernel for especificado, um kernel de 3x3 é usado por padrão.
- `anchor`: Posição do âncora no kernel; o padrão é o centro do kernel.
- `iterations`: Número de vezes que a operação de dilatação é aplicada. Mais iterações resultam em objetos mais dilatados.
- `borderType` e `borderValue`: Definem como a borda da imagem é tratada durante a operação.

A dilatação é frequentemente usada em combinação com a erosão, outra operação morfológica básica, para realizar tarefas como abertura, fechamento, e extração de bordas. A escolha do kernel e o número de iterações dependem do tamanho e da forma dos objetos na imagem e do resultado desejado.

---

**O que é Distance Transform?**

Na transformação de distância, os pixels de primeiro plano (geralmente brancos) em uma imagem binária são transformados de forma que cada pixel contém um número que indica a distância desse pixel até o pixel de fundo (geralmente preto) mais próximo. Essa distância pode ser calculada de diferentes maneiras, por exemplo, usando a distância Euclidiana, a distância de Manhattan, ou a distância de tabuleiro de xadrez.

**Funcionamento do cv2.distanceTransform**

A função `cv2.distanceTransform` é usada da seguinte forma:

```python
distanceImage = cv2.distanceTransform(src, distanceType, maskSize)
```

- `src`: A imagem binária de origem, onde os objetos são brancos e o fundo é preto.
- `distanceType`: O tipo de distância a ser usado. Pode ser `cv2.DIST_L2` para a distância Euclidiana, `cv2.DIST_L1` para a distância de Manhattan, ou `cv2.DIST_C` para a distância de tabuleiro de xadrez, entre outros.
- `maskSize`: O tamanho da máscara usada para a computação da distância. Afeta a precisão do resultado.

A imagem resultante (`distanceImage`) é uma imagem em tons de cinza onde os valores dos pixels representam as distâncias. Esta transformação é particularmente útil em várias aplicações, como:
- Segmentação de imagem e análise de forma, onde você precisa distinguir objetos que estão próximos uns dos outros.
- Processamento de imagens biomédicas, como a identificação de células ou outras estruturas.
- Navegação de robôs e planejamento de caminho, onde a distância aos objetos circundantes é crucial.
- Reconhecimento de padrões e visão computacional, para caracterizar a forma e a distribuição espacial dos objetos na imagem.


