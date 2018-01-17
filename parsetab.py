
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOLD BULLET CLEAN_TEXT CODE EMOJI HEADER1 HEADER2 HEADER3 HEADER4 HEADER5 HEADER6 IMAGE ITALIC LINK LSQUARE_PAREN NUM QUOTE RSQUARE_PAREN STRIKE TASK TEXT USERexpression : header \n                | bold \n                | italic\n                | strike\n                | user\n                | image\n                | bullet\n                | link\n                | quote\n                | emoji\n                | code\n                | num\n                | clean_textheader : LSQUARE_PAREN HEADER1  TEXT RSQUARE_PAREN\n            | LSQUARE_PAREN HEADER2  TEXT RSQUARE_PAREN\n            | LSQUARE_PAREN HEADER3  TEXT RSQUARE_PAREN\n            | LSQUARE_PAREN HEADER4  TEXT RSQUARE_PAREN\n            | LSQUARE_PAREN HEADER5  TEXT RSQUARE_PAREN\n            | LSQUARE_PAREN HEADER6  TEXT RSQUARE_PAREN\n    clean_text : CLEAN_TEXT\n                    | CLEAN_TEXT compound \n                    | CLEAN_TEXT compound TEXT\n                    | clean_text\n                    compound : bold \n                | italic\n                | strike\n                | user\n                | image\n                | link\n                | emoji\n                | bold clean_text\n                | italic clean_text\n                | strike clean_text\n                | user clean_text\n                | image clean_text\n                | link clean_text\n                | emoji clean_textbold : LSQUARE_PAREN BOLD TEXT RSQUARE_PARENitalic : LSQUARE_PAREN ITALIC TEXT RSQUARE_PARENstrike : LSQUARE_PAREN STRIKE TEXT RSQUARE_PARENuser : LSQUARE_PAREN USER TEXT RSQUARE_PAREN image : LSQUARE_PAREN IMAGE TEXT RSQUARE_PARENbullet : LSQUARE_PAREN BULLET TEXT RSQUARE_PARENlink : LSQUARE_PAREN LINK TEXT  RSQUARE_PARENquote : LSQUARE_PAREN QUOTE TEXT RSQUARE_PARENemoji : LSQUARE_PAREN EMOJI TEXT RSQUARE_PARENcode : LSQUARE_PAREN CODE TEXT RSQUARE_PARENnum : LSQUARE_PAREN NUM TEXT RSQUARE_PAREN'
    
_lr_action_items = {'STRIKE':([12,21,],[26,26,]),'HEADER1':([12,],[27,]),'HEADER5':([12,],[28,]),'USER':([12,21,],[41,41,]),'RSQUARE_PAREN':([51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,],[68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,]),'LINK':([12,21,],[32,32,]),'HEADER4':([12,],[33,]),'EMOJI':([12,21,],[34,34,]),'ITALIC':([12,21,],[35,35,]),'HEADER6':([12,],[36,]),'HEADER2':([12,],[40,]),'CLEAN_TEXT':([0,17,18,19,20,22,23,24,68,71,72,74,76,77,83,],[5,5,5,5,5,5,5,5,-40,-38,-42,-44,-46,-39,-41,]),'BOLD':([12,21,],[29,29,]),'IMAGE':([12,21,],[30,30,]),'LSQUARE_PAREN':([0,5,],[12,21,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,22,23,24,25,43,44,45,46,47,48,49,50,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,],[-8,0,-12,-6,-20,-13,-7,-5,-11,-3,-4,-9,-1,-10,-2,-29,-27,-25,-26,-28,-30,-24,-21,-23,-23,-23,-23,-23,-23,-23,-22,-40,-14,-18,-38,-42,-45,-44,-17,-46,-39,-19,-43,-16,-48,-15,-41,-47,]),'TEXT':([5,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,68,71,72,74,76,77,83,],[-20,-29,-27,-25,-26,-28,-30,-24,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,-23,-23,-23,-23,-23,-23,-23,-22,-40,-38,-42,-44,-46,-39,-41,]),'BULLET':([12,],[37,]),'HEADER3':([12,],[38,]),'NUM':([12,],[39,]),'QUOTE':([12,],[31,]),'CODE':([12,],[42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'user':([0,5,],[8,18,]),'link':([0,5,],[1,17,]),'header':([0,],[14,]),'italic':([0,5,],[10,19,]),'strike':([0,5,],[11,20,]),'image':([0,5,],[4,22,]),'compound':([5,],[25,]),'bold':([0,5,],[16,24,]),'expression':([0,],[2,]),'code':([0,],[9,]),'clean_text':([0,17,18,19,20,22,23,24,],[6,43,44,45,46,47,48,49,]),'bullet':([0,],[7,]),'emoji':([0,5,],[15,23,]),'quote':([0,],[13,]),'num':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> header','expression',1,'p_expression','easy_md_parser.py',16),
  ('expression -> bold','expression',1,'p_expression','easy_md_parser.py',17),
  ('expression -> italic','expression',1,'p_expression','easy_md_parser.py',18),
  ('expression -> strike','expression',1,'p_expression','easy_md_parser.py',19),
  ('expression -> user','expression',1,'p_expression','easy_md_parser.py',20),
  ('expression -> image','expression',1,'p_expression','easy_md_parser.py',21),
  ('expression -> bullet','expression',1,'p_expression','easy_md_parser.py',22),
  ('expression -> link','expression',1,'p_expression','easy_md_parser.py',23),
  ('expression -> quote','expression',1,'p_expression','easy_md_parser.py',24),
  ('expression -> emoji','expression',1,'p_expression','easy_md_parser.py',25),
  ('expression -> code','expression',1,'p_expression','easy_md_parser.py',26),
  ('expression -> num','expression',1,'p_expression','easy_md_parser.py',27),
  ('expression -> clean_text','expression',1,'p_expression','easy_md_parser.py',28),
  ('header -> LSQUARE_PAREN HEADER1 TEXT RSQUARE_PAREN','header',4,'p_header','easy_md_parser.py',34),
  ('header -> LSQUARE_PAREN HEADER2 TEXT RSQUARE_PAREN','header',4,'p_header','easy_md_parser.py',35),
  ('header -> LSQUARE_PAREN HEADER3 TEXT RSQUARE_PAREN','header',4,'p_header','easy_md_parser.py',36),
  ('header -> LSQUARE_PAREN HEADER4 TEXT RSQUARE_PAREN','header',4,'p_header','easy_md_parser.py',37),
  ('header -> LSQUARE_PAREN HEADER5 TEXT RSQUARE_PAREN','header',4,'p_header','easy_md_parser.py',38),
  ('header -> LSQUARE_PAREN HEADER6 TEXT RSQUARE_PAREN','header',4,'p_header','easy_md_parser.py',39),
  ('clean_text -> CLEAN_TEXT','clean_text',1,'p_clean_text','easy_md_parser.py',56),
  ('clean_text -> CLEAN_TEXT compound','clean_text',2,'p_clean_text','easy_md_parser.py',57),
  ('clean_text -> CLEAN_TEXT compound TEXT','clean_text',3,'p_clean_text','easy_md_parser.py',58),
  ('clean_text -> clean_text','clean_text',1,'p_clean_text','easy_md_parser.py',59),
  ('compound -> bold','compound',1,'p_compund','easy_md_parser.py',84),
  ('compound -> italic','compound',1,'p_compund','easy_md_parser.py',85),
  ('compound -> strike','compound',1,'p_compund','easy_md_parser.py',86),
  ('compound -> user','compound',1,'p_compund','easy_md_parser.py',87),
  ('compound -> image','compound',1,'p_compund','easy_md_parser.py',88),
  ('compound -> link','compound',1,'p_compund','easy_md_parser.py',89),
  ('compound -> emoji','compound',1,'p_compund','easy_md_parser.py',90),
  ('compound -> bold clean_text','compound',2,'p_compund','easy_md_parser.py',91),
  ('compound -> italic clean_text','compound',2,'p_compund','easy_md_parser.py',92),
  ('compound -> strike clean_text','compound',2,'p_compund','easy_md_parser.py',93),
  ('compound -> user clean_text','compound',2,'p_compund','easy_md_parser.py',94),
  ('compound -> image clean_text','compound',2,'p_compund','easy_md_parser.py',95),
  ('compound -> link clean_text','compound',2,'p_compund','easy_md_parser.py',96),
  ('compound -> emoji clean_text','compound',2,'p_compund','easy_md_parser.py',97),
  ('bold -> LSQUARE_PAREN BOLD TEXT RSQUARE_PAREN','bold',4,'p_bold','easy_md_parser.py',101),
  ('italic -> LSQUARE_PAREN ITALIC TEXT RSQUARE_PAREN','italic',4,'p_italic','easy_md_parser.py',106),
  ('strike -> LSQUARE_PAREN STRIKE TEXT RSQUARE_PAREN','strike',4,'p_strike','easy_md_parser.py',112),
  ('user -> LSQUARE_PAREN USER TEXT RSQUARE_PAREN','user',4,'p_user','easy_md_parser.py',118),
  ('image -> LSQUARE_PAREN IMAGE TEXT RSQUARE_PAREN','image',4,'p_image','easy_md_parser.py',124),
  ('bullet -> LSQUARE_PAREN BULLET TEXT RSQUARE_PAREN','bullet',4,'p_bullet','easy_md_parser.py',130),
  ('link -> LSQUARE_PAREN LINK TEXT RSQUARE_PAREN','link',4,'p_link','easy_md_parser.py',136),
  ('quote -> LSQUARE_PAREN QUOTE TEXT RSQUARE_PAREN','quote',4,'p_quote','easy_md_parser.py',142),
  ('emoji -> LSQUARE_PAREN EMOJI TEXT RSQUARE_PAREN','emoji',4,'p_emoji','easy_md_parser.py',148),
  ('code -> LSQUARE_PAREN CODE TEXT RSQUARE_PAREN','code',4,'p_code','easy_md_parser.py',154),
  ('num -> LSQUARE_PAREN NUM TEXT RSQUARE_PAREN','num',4,'p_num','easy_md_parser.py',160),
]
