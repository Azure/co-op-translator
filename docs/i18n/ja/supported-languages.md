# サポートされている言語

Co-op Translator はテキスト、ノートブック、画像の翻訳出力に対して以下の言語コードをサポートしています。

新しい言語を追加したい場合は、`src/co_op_translator/fonts/` 以下の言語およびフォントのマッピングを更新し、プルリクエストを開く前に言語をテストしてください。

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | 英語 | NotoSans-Medium.ttf | いいえ | なし |
| fr | フランス語 | NotoSans-Medium.ttf | いいえ | なし |
| es | スペイン語 | NotoSans-Medium.ttf | いいえ | なし |
| de | ドイツ語 | NotoSans-Medium.ttf | いいえ | なし |
| ru | ロシア語 | NotoSans-Medium.ttf | いいえ | なし |
| ar | アラビア語 | NotoSansArabic-Medium.ttf | はい | なし |
| fa | ペルシア語（ファルシ） | NotoSansArabic-Medium.ttf | はい | なし |
| ur | ウルドゥー語 | NotoSansArabic-Medium.ttf | はい | なし |
| zh-CN | 中国語（簡体字） | NotoSansCJK-Medium.ttc | いいえ | なし |
| zh-MO | 中国語（繁体字、マカオ） | NotoSansCJK-Medium.ttc | いいえ | なし |
| zh-HK | 中国語（繁体字、香港） | NotoSansCJK-Medium.ttc | いいえ | なし |
| zh-TW | 中国語（繁体字、台湾） | NotoSansCJK-Medium.ttc | いいえ | なし |
| ja | 日本語 | NotoSansCJK-Medium.ttc | いいえ | なし |
| ko | 韓国語 | NotoSansCJK-Medium.ttc | いいえ | なし |
| hi | ヒンディー語 | NotoSansDevanagari-Medium.ttf | いいえ | なし |
| bn | ベンガル語 | NotoSansBengali-Medium.ttf | いいえ | なし |
| mr | マラーティー語 | NotoSansDevanagari-Medium.ttf | いいえ | なし |
| ne | ネパール語 | NotoSansDevanagari-Medium.ttf | いいえ | なし |
| pa | パンジャブ語（グルムキー） | NotoSansGurmukhi-Medium.ttf | いいえ | なし |
| pt-PT | ポルトガル語（ポルトガル） | NotoSans-Medium.ttf | いいえ | なし |
| pt-BR | ポルトガル語（ブラジル） | NotoSans-Medium.ttf | いいえ | なし |
| it | イタリア語 | NotoSans-Medium.ttf | いいえ | なし |
| lt | リトアニア語 | NotoSans-Medium.ttf | いいえ | なし |
| pl | ポーランド語 | NotoSans-Medium.ttf | いいえ | なし |
| tr | トルコ語 | NotoSans-Medium.ttf | いいえ | なし |
| el | ギリシャ語 | NotoSans-Medium.ttf | いいえ | なし |
| th | タイ語 | NotoSansThai-Medium.ttf | いいえ | なし |
| sv | スウェーデン語 | NotoSans-Medium.ttf | いいえ | なし |
| da | デンマーク語 | NotoSans-Medium.ttf | いいえ | なし |
| no | ノルウェー語 | NotoSans-Medium.ttf | いいえ | なし |
| fi | フィンランド語 | NotoSans-Medium.ttf | いいえ | なし |
| nl | オランダ語 | NotoSans-Medium.ttf | いいえ | なし |
| he | ヘブライ語 | NotoSansHebrew-Medium.ttf | はい | なし |
| vi | ベトナム語 | NotoSans-Medium.ttf | いいえ | なし |
| id | インドネシア語 | NotoSans-Medium.ttf | いいえ | なし |
| ms | マレー語 | NotoSans-Medium.ttf | いいえ | なし |
| tl | タガログ語（フィリピン） | NotoSans-Medium.ttf | いいえ | なし |
| sw | スワヒリ語 | NotoSans-Medium.ttf | いいえ | なし |
| hu | ハンガリー語 | NotoSans-Medium.ttf | いいえ | なし |
| cs | チェコ語 | NotoSans-Medium.ttf | いいえ | なし |
| sk | スロバキア語 | NotoSans-Medium.ttf | いいえ | なし |
| ro | ルーマニア語 | NotoSans-Medium.ttf | いいえ | なし |
| bg | ブルガリア語 | NotoSans-Medium.ttf | いいえ | なし |
| sr | セルビア語（キリル） | NotoSans-Medium.ttf | いいえ | なし |
| hr | クロアチア語 | NotoSans-Medium.ttf | いいえ | なし |
| sl | スロベニア語 | NotoSans-Medium.ttf | いいえ | なし |
| uk | ウクライナ語 | NotoSans-Medium.ttf | いいえ | なし |
| my | ビルマ語（ミャンマー） | NotoSansMyanmar-Medium.ttf | いいえ | なし |
| ta | タミル語 | NotoSansTamil-Medium.ttf | いいえ | なし |
| et | エストニア語 | NotoSans-Medium.ttf | いいえ | なし |
| pcm | ナイジェリア・ピジン語 | NotoSans-Medium.ttf | いいえ | なし |
| te | テルグ語 | NotoSans-Medium.ttf | いいえ | なし |
| ml | マラヤーラム語 | NotoSans-Medium.ttf | いいえ | なし |
| kn | カンナダ語 | NotoSans-Medium.ttf | いいえ | なし |
| km | クメール語 | NotoSansKhmer-Medium.ttf | いいえ | なし |

## 言語の追加

新しい言語をサポートに追加するには:

1. 言語ユーティリティに言語コードと表示名を追加します。
2. フォントを `src/co_op_translator/fonts/font_language_mappings.yml` に追加またはマッピングします。
3. Markdown と画像の翻訳結果をテストします。
4. マッピングと検証のメモを添えてプルリクエストを作成します。