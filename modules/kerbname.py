import random
import willie

names = {
	'proper': 
		['Adam', 'Al', 'Alan', 'Archibald', 'Buzz', 'Carson', 'Chad', 'Charlie', 'Chris', 'Chuck', 'Dean', 'Ed', 'Edan', 'Edlu', 'Frank', 'Franklin', 'Gus', 'Hans', 'Jack', 'James', 'Jim', 'Kirk', 'Kurt', 'Lars', 'Luke', 'Mac', 'Matt', 'Phil', 'Randall', 'Scott', 'Scott', 'Sean', 'Steve', 'Tom', 'Will'], 
	'pref': 
		['Ad', 'Al', 'Ald', 'An', 'Bar', 'Bart', 'Bil', 'Billy-Bob', 'Bob', 'Bur', 'Cal', 'Cam', 'Chad', 'Cor', 'Dan', 'Der', 'Des', 'Dil', 'Do', 'Don', 'Dood', 'Dud', 'Dun', 'Ed', 'El', 'En', 'Er', 'Fer', 'Fred', 'Gene', 'Geof', 'Ger', 'Gil', 'Greg', 'Gus', 'Had', 'Hal', 'Han', 'Har', 'Hen', 'Her', 'Hud', 'Jed', 'Jen', 'Jer', 'Joe', 'John', 'Jon', 'Jor', 'Kel', 'Ken', 'Ker', 'Kir', 'Lan', 'Lem', 'Len', 'Lo', 'Lod', 'Lu', 'Lud', 'Mac', 'Mal', 'Mat', 'Mel', 'Mer', 'Mil', 'Mit', 'Mun', 'Ned', 'Neil', 'Nel', 'New', 'Ob', 'Or', 'Pat', 'Phil', 'Ray', 'Rib', 'Rich', 'Ro', 'Rod', 'Ron', 'Sam', 'Sean', 'See', 'Shel', 'Shep', 'Sher', 'Sid', 'Sig', 'Son', 'Thom', 'Thomp', 'Tom', 'Wehr', 'Wil'], 
	'suf': 
		['ald', 'bal', 'bald', 'bart', 'bas', 'berry', 'bert', 'bin', 'ble', 'bles', 'bo', 'bree', 'brett', 'bro', 'bur', 'burry', 'bus', 'by', 'cal', 'can', 'cas', 'cott', 'dan', 'das', 'den', 'din', 'do', 'don', 'dorf', 'dos', 'dous', 'dred', 'drin', 'dun', 'ely', 'emone', 'emy', 'eny', 'fal', 'fel', 'fen', 'field', 'ford', 'fred', 'frey', 'frey', 'frid', 'frod', 'fry', 'furt', 'gan', 'gard', 'gas', 'gee', 'gel', 'ger', 'gun', 'hat', 'ing', 'ke', 'kin', 'lan', 'las', 'ler', 'ley', 'lie', 'lin', 'lin', 'lo', 'lock', 'long', 'lorf', 'ly', 'mal', 'man', 'min', 'ming', 'mon', 'more', 'mund', 'my', 'nand', 'nard', 'ner', 'ney', 'nie', 'ny', 'oly', 'ory', 'rey', 'rick', 'rie', 'righ', 'rim', 'rod', 'ry', 'sby', 'sel', 'sen', 'sey', 'ski', 'son', 'sted', 'ster', 'sy', 'ton', 'top', 'trey', 'van', 'vey', 'vin', 'vis', 'well', 'wig', 'win', 'wise', 'zer', 'zon', 'zor']
	}

@willie.module.commands('kerbname', 'kerbal', 'kerman')
def kerbname(bot, trigger):
	'''generates a random name for a kerbal'''
	if random.random() <= 0.05:
		name = random.choice(names['proper'])
	else:
		name = random.choice(names['pref']) + random.choice(names['suf'])
	bot.reply(name + ' Kerman')

