#!venv/bin/python
from bs4 import BeautifulSoup
from sys import stdin, stderr
from click import command


@command('pol2val', help='Put html page from polygon/tests in stdin. Page must contain #testGroupsTable table.')
def main():
	TAB = ' ' * 4
	bs = BeautifulSoup(stdin.read(), features='lxml')
	table = bs.select('#testGroupsTable > tbody > tr')
	test = 1
	for row in table:
		cols = row.select('td')
		group, tests, score, policy, _, requires, _ = cols
		group = int(group.text.strip())
		tests = int(tests.text.strip())
		score = int(score.text.strip())
		print(f'group {group}', '{')
		print(f'{TAB}tests {test}-{test + int(tests) - 1};')
		test += tests
		if policy.select(f'#view-dependence-value-{group}')[0].text.strip() == 'COMPLETE_GROUP':
			print(f'{TAB}score {score};')
		else:
			print(f'{TAB}test_score {score // tests};')
		x = list(map(lambda x: x.text.strip(), filter(lambda x: x.get('style') != 'display:none;', requires.select('div > span'))))
		print(f'{TAB}requires {",".join(x)};') if x else None
		print('}')
		print()


if __name__ == '__main__':
	main()
