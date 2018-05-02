\set ON_ERROR_STOP ON
\c ah8210
drop database if exists cudb;
create database cudb;
\c cudb;

	-- Tabell med två kolumner; användarnamn och lösenord.
CREATE TABLE user_password (
 	--Ser till att användarnamnet är unikt.
	email VARCHAR(100) PRIMARY KEY,	
 	password VARCHAR(100)
);

	--Varje kodrad motsvarar en rad i tabellen "user_password". Dvs varje användarnamn skall höra ihop med ett lösenord.
Insert INTO user_password values
	('test@gmail.com', 'lösenord1'),
	('test@hotmail.com', 'lösenord1'),
	('TESTING@gmail.com', 'lösen')
;

	-- Tabell med två kolumner; städföremål och rum.
CREATE TABLE items (
  name TEXT,
  room TEXT
);

	--Varje kodrad motsvarar en rad i tabellen "items". Dvs varje städföremål skall höra ihop med ett rum.
Insert INTO items values
	-- Kök
	('ugn', 'kök'),
	('diskbänk', 'kök'),
	('spis', 'kök'),
	('spisfläkt', 'kök'),
	('bord', 'kök'),
	('köksluckor', 'kök'),
	('kylskåp', 'kök'),
	('frys', 'kök'),
	('mikrovågsugn', 'kök'),
	('brödrost', 'kök'),
	('kaffebryggare', 'kök'),
	('diskmaskin', 'kök'),
	('skafferi', 'kök'),
	-- Sovrum
	('säng', 'sovrum'),
	('byrå', 'sovrum'),
	('garderob', 'sovrum'),
	('nattduksbord', 'sovrum'),
	-- Vardagsrum
	('soffa', 'vardagsrum'),
	('fotölj', 'vardagsrum'),
	('tv', 'vardagsrum'),
	('tv-bänk', 'vardagsrum'),
	('soffbord', 'vardagsrum'),
	('matbord', 'vardagsrum'),
	('bokhylla', 'vardagsrum'),
	('fotpall', 'vardagsrum'),
	-- Badrum
	('badkar', 'badrum'),
	('toalett', 'badrum'),
	('handfat', 'badrum'),
	('vattenlås', 'badrum'),
	('badrumsmatta', 'badrum'),
	('badrumsspegel', 'badrum'),
	('medicinskåp', 'badrum'),
	('tvättmaskin', 'badrum'),
	('torktumlare', 'badrum'),
	('golvbrunn', 'badrum'),
	-- Arbetsrum
	('skrivbord', 'arbetsrum'),
	('bokhylla', 'arbetsrum'),
	-- Hall
	('skohylla', 'hall'),
	('spegel', 'hall'),
	('hatthylla', 'hall'),
	('dörrmatta', 'hall'),
	-- Gemensamma föremål
	('golv', 'alla'),
	('vägg', 'alla'),
	('fönster', 'alla'),
	('lister', 'alla'),
	('element', 'alla'),
	('lampa', 'alla'),
	('matta', 'alla'),
	('duk', 'alla'),
	('växt', 'alla'),
	('gardin', 'alla'),
	('persienner', 'alla'),
	('tavla', 'alla')
;

	-- Tabell med två kolumner; föremål och föremålets syfte.
CREATE TABLE cleaning_items (
	name TEXT,
	utility TEXT
);

	--Varje kodrad motsvarar en rad i tabellen "cleaning_items". Dvs varje föremål skall höra ihop med ett syfte.
Insert INTO cleaning_items values
	-- Städverktyg & städmedel
	('kvast', 'utility'),
	('toalettborste', 'utility'),
	('stålull', 'utility'),
	('disktrasa', 'utility'),
	('moppmedhink', 'utility'),
	('våttork', 'utility'),
	('dammsugare', 'utility'),
	('skyffelborste', 'utility'),
	('dammvippa', 'utility'),
	('mikrofibertrasa', 'utility'),
	('tvättsvamp', 'utility'),
	('skurmedel', 'utility'),
	('diskmedel', 'utility'),
	('fönstertvätt', 'utility'),
	('såpa', 'utility'),
	('wc-anka', 'utility'),
	('handsprit', 'utility'),
	('rengöringsmedel', 'utility')
;
