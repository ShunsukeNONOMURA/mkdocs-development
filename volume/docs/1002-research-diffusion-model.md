# 研究：Diffusion Model

## 画像生成AI
22年12月に公開された日本経済新聞の「[AIが描く絵 見分けられる?](https://vdata.nikkei.com/newsgraphics/ai-art/)」のように人間が作成したものかどうかの区別が難しくなるほど近年の画像生成AIの進化はめざましいものがある。  
サービスとして公開されているものは以下のものが代表される

- [Midjourney](https://www.midjourney.com/home/)
- [NovelAI](https://novelai.net/)
- [Leonardo.Ai](https://leonardo.ai/)

## Diffusion Model(拡散モデル) 
[High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)で提唱されている画像生成手法。
主に下記のような特徴を有する。

- forward process（拡散過程）とreverse process（逆拡散過程）を用いて画像とノイズ間の変換を行う
    - forward process
        - 画像にノイズを加えながら、最終的にノイズ画像を生成する確率過程
    - reverse process
        - forward processの逆をたどることで画像を生成する確率過程
        - U-Netを用いる
- 画像生成する場合
    - **乱数生成したノイズ画像に対してreverse processを実行して反復的にノイズを取り除くことで画像を生成する**
        - reverse processごとに潜在空間でベクトル化したConditioningの**text**や**画像**をconcatすることで、生成内容に指向性を持たせる
    - 最終的に逆拡散後の潜在空間ノイズにVAE(Variational Autoencoder) Decorderをかけて、画像に戻す。
- 参考
    - [世界に衝撃を与えた画像生成AI「Stable Diffusion」を徹底解説！](https://qiita.com/omiita/items/ecf8d60466c50ae8295b)
    - [【論文解説】Diffusion Modelを理解する](https://data-analytics.fun/2022/02/03/understanding-diffusion-model/)
    - [Computer Vision & Learning Group](https://ommer-lab.com/research/latent-diffusion-models/)

### Diffusion Model

![](https://ommer-lab.com/wp-content/uploads/2022/08/article-Figure3-1-1024x508.png)

### reverse process（逆拡散過程）のイメージ
U-Netの出力は潜在空間ノイズなので厳密には画像ではないことに注意すること。  
画像化するときはVAEを用いて潜在空間ノイズから変換する。

![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fi.imgur.com%2FBRUncxB.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=1b104d38498660c2084087972ced9e26)

### forward process と reverse process の関係

![](https://data-analytics.fun/wp-content/uploads/2022/02/image-12-768x489.png)
