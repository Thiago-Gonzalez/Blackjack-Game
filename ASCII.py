cards_ascii = ['''
 ------------- 
|K♥           |
|   -------   |
|  |♥      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♥|  |
|   -------   |
|           ♥K|
 ------------- ''', '''
 ------------- 
|Q♥           |
|   -------   |
|  |♥      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♥|  |
|   -------   |
|           ♥Q|
 ------------- ''', '''
 ------------- 
|J♥           |
|   -------   |
|  |♥      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♥|  |
|   -------   |
|           ♥J|
 ------------- ''', '''
 ------------- 
|10♥          |
|   -------   |
|  |♥     ♥|  |
|  |   ♥   |  |
|  |♥     ♥|  |
|  |       |  |
|  |♥     ♥|  |
|  |   ♥   |  |
|  |♥     ♥|  |
|   -------   |
|          ♥10|
 ------------- ''', '''
 ------------- 
|9♥           |
|   -------   |
|  |♥     ♥|  |
|  |       |  |
|  |♥     ♥|  |
|  |   ♥   |  |
|  |♥     ♥|  |
|  |       |  |
|  |♥     ♥|  |
|   -------   |
|           ♥9|
 ------------- ''', '''
 ------------- 
|8♥           |
|   -------   |
|  |♥     ♥|  |
|  |   ♥   |  |
|  |       |  |
|  |♥     ♥|  |
|  |       |  |
|  |   ♥   |  |
|  |♥     ♥|  |
|   -------   |
|           ♥8|
 ------------- ''', '''
 ------------- 
|7♥           |
|   -------   |
|  |♥     ♥|  |
|  |   ♥   |  |
|  |       |  |
|  |♥     ♥|  |
|  |       |  |
|  |       |  |
|  |♥     ♥|  |
|   -------   |
|           ♥7|
 ------------- ''', '''
 ------------- 
|6♥           |
|   -------   |
|  |♥     ♥|  |
|  |       |  |
|  |       |  |
|  |♥     ♥|  |
|  |       |  |
|  |       |  |
|  |♥     ♥|  |
|   -------   |
|           ♥6|
 ------------- ''', '''
 ------------- 
|5♥           |
|   -------   |
|  |♥     ♥|  |
|  |       |  |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|  |       |  |
|  |♥     ♥|  |
|   -------   |
|           ♥5|
 ------------- ''', '''
 ------------- 
|4♥           |
|   -------   |
|  |♥     ♥|  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |♥     ♥|  |
|   -------   |
|           ♥4|
 ------------- ''', '''
 ------------- 
|3♥           |
|   -------   |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|   -------   |
|           ♥3|
 ------------- ''', '''
 ------------- 
|2♥           |
|   -------   |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|   -------   |
|           ♥2|
 ------------- ''', '''
 ------------- 
|A♥           |
|   -------   |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♥   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|   -------   |
|           ♥A|
 ------------- ''', '''
 ------------- 
|K♦           |
|   -------   |
|  |♦      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♦|  |
|   -------   |
|           ♦K|
 ------------- ''', '''
 ------------- 
|Q♦           |
|   -------   |
|  |♦      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♦|  |
|   -------   |
|           ♦Q|
 ------------- ''', '''
 ------------- 
|J♦           |
|   -------   |
|  |♦      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♦|  |
|   -------   |
|           ♦J|
 ------------- ''', '''
 ------------- 
|10♦          |
|   -------   |
|  |♦     ♦|  |
|  |   ♦   |  |
|  |♦     ♦|  |
|  |       |  |
|  |♦     ♦|  |
|  |   ♦   |  |
|  |♦     ♦|  |
|   -------   |
|          ♦10|
 ------------- ''', '''
 ------------- 
|9♦           |
|   -------   |
|  |♦     ♦|  |
|  |       |  |
|  |♦     ♦|  |
|  |   ♦   |  |
|  |♦     ♦|  |
|  |       |  |
|  |♦     ♦|  |
|   -------   |
|           ♦9|
 ------------- ''', '''
 ------------- 
|8♦           |
|   -------   |
|  |♦     ♦|  |
|  |   ♦   |  |
|  |       |  |
|  |♦     ♦|  |
|  |       |  |
|  |   ♦   |  |
|  |♦     ♦|  |
|   -------   |
|           ♦8|
 ------------- ''', '''
 ------------- 
|7♦           |
|   -------   |
|  |♦     ♦|  |
|  |   ♦   |  |
|  |       |  |
|  |♦     ♦|  |
|  |       |  |
|  |       |  |
|  |♦     ♦|  |
|   -------   |
|           ♦7|
 ------------- ''', '''
 ------------- 
|6♦           |
|   -------   |
|  |♦     ♦|  |
|  |       |  |
|  |       |  |
|  |♦     ♦|  |
|  |       |  |
|  |       |  |
|  |♦     ♦|  |
|   -------   |
|           ♦6|
 ------------- ''', '''
 ------------- 
|5♦           |
|   -------   |
|  |♦     ♦|  |
|  |       |  |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|  |       |  |
|  |♦     ♦|  |
|   -------   |
|           ♦5|
 ------------- ''', '''
 ------------- 
|4♦           |
|   -------   |
|  |♦     ♦|  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |♦     ♦|  |
|   -------   |
|           ♦4|
 ------------- ''', '''
 ------------- 
|3♦           |
|   -------   |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|   -------   |
|           ♦3|
 ------------- ''', '''
 ------------- 
|2♦           |
|   -------   |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|   -------   |
|           ♦2|
 ------------- ''', '''
 ------------- 
|A♦           |
|   -------   |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♦   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|   -------   |
|           ♦A|
 ------------- ''', '''
 ------------- 
|K♣           |
|   -------   |
|  |♣      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♣|  |
|   -------   |
|           ♣K|
 ------------- ''', '''
 ------------- 
|Q♣           |
|   -------   |
|  |♣      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♣|  |
|   -------   |
|           ♣Q|
 ------------- ''', '''
 ------------- 
|J♣           |
|   -------   |
|  |♣      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♣|  |
|   -------   |
|           ♣J|
 ------------- ''', '''
 ------------- 
|10♣          |
|   -------   |
|  |♣     ♣|  |
|  |   ♣   |  |
|  |♣     ♣|  |
|  |       |  |
|  |♣     ♣|  |
|  |   ♣   |  |
|  |♣     ♣|  |
|   -------   |
|          ♣10|
 ------------- ''', '''
 ------------- 
|9♣           |
|   -------   |
|  |♣     ♣|  |
|  |       |  |
|  |♣     ♣|  |
|  |   ♣   |  |
|  |♣     ♣|  |
|  |       |  |
|  |♣     ♣|  |
|   -------   |
|           ♣9|
 ------------- ''', '''
 ------------- 
|8♣           |
|   -------   |
|  |♣     ♣|  |
|  |   ♣   |  |
|  |       |  |
|  |♣     ♣|  |
|  |       |  |
|  |   ♣   |  |
|  |♣     ♣|  |
|   -------   |
|           ♣8|
 ------------- ''', '''
 ------------- 
|7♣           |
|   -------   |
|  |♣     ♣|  |
|  |   ♣   |  |
|  |       |  |
|  |♣     ♣|  |
|  |       |  |
|  |       |  |
|  |♣     ♣|  |
|   -------   |
|           ♣7|
 ------------- ''', '''
 ------------- 
|6♣           |
|   -------   |
|  |♣     ♣|  |
|  |       |  |
|  |       |  |
|  |♣     ♣|  |
|  |       |  |
|  |       |  |
|  |♣     ♣|  |
|   -------   |
|           ♣6|
 ------------- ''', '''
 ------------- 
|5♣           |
|   -------   |
|  |♣     ♣|  |
|  |       |  |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|  |       |  |
|  |♣     ♣|  |
|   -------   |
|           ♣5|
 ------------- ''', '''
 ------------- 
|4♣           |
|   -------   |
|  |♣     ♣|  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |♣     ♣|  |
|   -------   |
|           ♣4|
 ------------- ''', '''
 ------------- 
|3♣           |
|   -------   |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|   -------   |
|           ♣3|
 ------------- ''', '''
 ------------- 
|2♣           |
|   -------   |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|   -------   |
|           ♣2|
 ------------- ''', '''
 ------------- 
|A♣           |
|   -------   |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♣   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|   -------   |
|           ♣A|
 ------------- ''', '''
 ------------- 
|K♠           |
|   -------   |
|  |♠      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♠|  |
|   -------   |
|           ♠K|
 ------------- ''', '''
 ------------- 
|Q♠           |
|   -------   |
|  |♠      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♠|  |
|   -------   |
|           ♠Q|
 ------------- ''', '''
 ------------- 
|J♠           |
|   -------   |
|  |♠      |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |      ♠|  |
|   -------   |
|           ♠J|
 ------------- ''', '''
 ------------- 
|10♠          |
|   -------   |
|  |♠     ♠|  |
|  |   ♠   |  |
|  |♠     ♠|  |
|  |       |  |
|  |♠     ♠|  |
|  |   ♠   |  |
|  |♠     ♠|  |
|   -------   |
|          ♠10|
 ------------- ''', '''
 ------------- 
|9♠           |
|   -------   |
|  |♠     ♠|  |
|  |       |  |
|  |♠     ♠|  |
|  |   ♠   |  |
|  |♠     ♠|  |
|  |       |  |
|  |♠     ♠|  |
|   -------   |
|           ♠9|
 ------------- ''', '''
 ------------- 
|8♠           |
|   -------   |
|  |♠     ♠|  |
|  |   ♠   |  |
|  |       |  |
|  |♠     ♠|  |
|  |       |  |
|  |   ♠   |  |
|  |♠     ♠|  |
|   -------   |
|           ♠8|
 ------------- ''', '''
 ------------- 
|7♠           |
|   -------   |
|  |♠     ♠|  |
|  |   ♠   |  |
|  |       |  |
|  |♠     ♠|  |
|  |       |  |
|  |       |  |
|  |♠     ♠|  |
|   -------   |
|           ♠7|
 ------------- ''', '''
 ------------- 
|6♠           |
|   -------   |
|  |♠     ♠|  |
|  |       |  |
|  |       |  |
|  |♠     ♠|  |
|  |       |  |
|  |       |  |
|  |♠     ♠|  |
|   -------   |
|           ♠6|
 ------------- ''', '''
 ------------- 
|5♠           |
|   -------   |
|  |♠     ♠|  |
|  |       |  |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|  |       |  |
|  |♠     ♠|  |
|   -------   |
|           ♠5|
 ------------- ''', '''
 ------------- 
|4♠           |
|   -------   |
|  |♠     ♠|  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |♠     ♠|  |
|   -------   |
|           ♠4|
 ------------- ''', '''
 ------------- 
|3♠           |
|   -------   |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|   -------   |
|           ♠3|
 ------------- ''', '''
 ------------- 
|2♠           |
|   -------   |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|   -------   |
|           ♠2|
 ------------- ''', '''
 ------------- 
|A♠           |
|   -------   |
|  |       |  |
|  |       |  |
|  |       |  |
|  |   ♠   |  |
|  |       |  |
|  |       |  |
|  |       |  |
|   -------   |
|           ♠A|
 ------------- ''', '''
 -------------
| * * * * * * |
|* * * * * * *|
| * * * * * * |
|* * * * * * *|
| * * * * * * |
|* * * * * * *|
| * * * * * * |
|* * * * * * *|
| * * * * * * | 
|* * * * * * *|
 ------------- ''']
