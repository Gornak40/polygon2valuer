#!venv/bin/python
from bs4 import BeautifulSoup
from sys import stdin, stderr
from click import command, option


@command('pol2val', help='Put html page from polygon/tests in stdin. Page must contain #testGroupsTable table.')
@option('--scoring', '-s', is_flag=True, help='Create scoring.tex temlpate.')
def main(scoring):
	TAB = ' ' * 4
	bs = BeautifulSoup(stdin.read(), features='lxml')
	table = bs.select('#testGroupsTable > tbody > tr')
	test = 1
	if scoring:
		with open('scoring.tex', 'w') as sfile:
			print('\\begin{center}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{tabular}{|c|c|c|c|}\n\\hline', file=sfile)
			print('\\textbf{Группа} & \\textbf{Баллы} & \\textbf{Доп. ограничения} & \\textbf{Необх. группы} \\\\ \\hline', file=sfile)
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
		if scoring:
			with open('scoring.tex', 'a') as sfile:
				print(f'${group}$ & ${score}$ & {"тесты из условия" if group == 0 else ""} & {"---" if not x else ", ".join(map(lambda y: "$" + y + "$", x))} \\\\ \\hline', file=sfile)
		print(f'{TAB}requires {",".join(x)};') if x else None
		print('}')
		print()
	if scoring:
		with open('scoring.tex', 'a') as sfile:
			print('\\end{tabular}\n\\end{center}\n', file=sfile)


if __name__ == '__main__':
	main()
