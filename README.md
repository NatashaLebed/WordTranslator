# WordTranslator
JetBrain Study Project

Takes arguments from the command line, translates word from and to one of the languages(or to all of them), saves translations and examples of context use to file <word>.txt

languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
             'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']
## Examples:

===============================================================
### Input:
  `python main.py english japanese book`
---------------------------------------------------------------
### Output (book.txt):
#### Japanese Translations:
  - ブック
  - 予約
  - 帳
  - 書
  - 書籍

#### Japanese Examples:
- Bargiacchi's book reflects this dual nature.
- Bargiacchiの本は、この二重の性質を反映し.

- I've not found a bad O'Reilly book yet.
- 私はまだ　O｀Reilly　でダメな本を見たことがありません。

- Briefing book pages provide %s data analysis features.
- ブリーフィング　ブック　ページでは、%s　データ分析機能を使用できます。

- The briefing book is not locked.
- ブリーフィング　ブックはロックされていません。

- It is recommended to book Fjærlandsfjord fjord cruise tickets in advance.
- Fjærlandsfjordのフィヨルドクルーズチケットは前もって予約することをお奨めします。

===============================================================
### Input:
  `python main.py english all tree` 
---------------------------------------------------------------
### Output (tree.txt):

#### Arabic Translations:
تري

#### Arabic Examples:
- Ritchie and Liz spotted in tree.
- Edie, see that Christmas tree?


#### German Translations:
Struktur

#### German Examples:
- Expand a node in the Troubleshooter tree.
- Erweitern Sie einen Knoten im Baum Fehlerbeheber (Troubleshooter).


#### Spanish Translations:
higuera

#### Spanish Examples:
- There, under the half-fallen tree.
- Allí, bajo el árbol a medio caer.


#### French Translations:
sapin

#### French Examples:
- Apply this decision tree template to create your own diagram.
- Appliquer ce modèle d'arbre de décision pour créer votre propre schéma.


#### Hebrew Translations:
אילן

#### Hebrew Examples:
- Failed to construct a huffman tree using the length array. The stream might be corrupted.
- The specified member is not associated with the same MetadataWorkspace or data space as the command tree.


#### Japanese Translations:
木

#### Japanese Examples:
- Returns current (selected) checkbox tree item.
- 現在の　（選択されている）　チェックボックスツリーアイテムを返します。


#### Dutch Translations:
stamboom

#### Dutch Examples:
- Even your tree shows imagination and resourcefulness...
- De boom is een toonbeeld van fantasie en vindingrijkheid.


#### Polish Translations:
choinka

#### Polish Examples:
- And then I climbed back up the tree.
- A potem znowu wspialem sie na drzewo i tym razem mi sie udalo, wszedlem.


#### Portuguese Translations:
figueira

#### Portuguese Examples:
- Zee once mentioned this medicinal tree sap.
- A Zee uma vez mencionou a seiva de árvore como sendo medicinal.


#### Romanian Translations:
pom

#### Romanian Examples:
- A tree grew strong and tall.
- Un copac care a crescut puternic și înalt.


#### Russian Translations:
елка

#### Russian Examples:
- He magically recovered after being impaled by a tree.
- Он волшебным образом выжил после того, как его проткнуло дерево.


#### Turkish Translations:
ahşap

#### Turkish Examples:
- Only a fulfilled tree will flower.
- Yalnızca bütün olarak yaşayan bir ağaç çiçek verebilir.

