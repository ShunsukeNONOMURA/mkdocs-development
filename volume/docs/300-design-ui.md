# （記述中）設計：UI設計

## コンポーネント駆動開発(CDD)
UIを組み上げるときにコンポーネントから作り、最後にページを作り上げる「ボトムアップ」の開発プロセスのこと。  

## Atomic Design
- CDDにおける命名や粒度の一指標
- 原子（atoms）、分子（molecules）、組織（organisms）、テンプレート（template）、ページ（page）
- 粒度軸区別なので曖昧さがある
    - ラベル付きのボタンはatomsなのかmoleculesなのか
    - アイコン付き入力フォーム（フォーム＋ボタン＋アイコン）はmoleculesなのかorganismsなのか
    - 曖昧さが循環参照リスクになる

## BCD Design
- 粒度軸ではなく、概念軸（Base Case Domain）で切り分けることで曖昧性を廃する
- [Vuetify](https://vuetifyjs.com/)のような汎用コンポーネントは基本的にBaseコンポーネントにあたる。

## 参考
- CDD
    - [Component Driven User Interfaces](https://www.componentdriven.org/)
- Atomic Design
    - [Atomic Design Methodology](https://atomicdesign.bradfrost.com/chapter-2/)
- BCD Design
    - [BCD Design によるコンポーネントの分類](https://qiita.com/misuken/items/19f9f603ab165e228fe1)


<!--

## Atomic Design
- [UI 開発をアジャイルに行うための Atomic Design](https://www.slideshare.net/ygoto3q/atomic-design-for-agile-ui-development-100961721)
- [（穴あり版） UI 開発をアジャイルに行うための Atomic Design](https://www.slideshare.net/ygoto3q/atomic-design-for-agile-ui-development-100929591)

-->>