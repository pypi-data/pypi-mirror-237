import contextlib, copy, json, os, scrabble, string, sys, typing

wordlist_full = list(copy.deepcopy(scrabble.scrabble.config.ENGLISH_DICTIONARY_SET))

def build_letter_scores(
	name: str
) -> typing.Dict[str, int]:
	return next(
		(
			val
			for key, val in {
				'quarrel': {
					'a': 1, 'b': 5, 'c': 2, 'd': 3, 'e': 1, 'f': 5, 'g': 4,
					'h': 4, 'i': 1, 'j': 15, 'k': 6, 'l': 2, 'm': 4, 'n': 1,
					'o': 1, 'p': 3, 'q': 15, 'r': 2, 's': 1, 't': 1, 'u': 3,
					'v': 6, 'w': 5, 'x': 10, 'y': 5, 'z': 12
				},
				'scrabble': {
					'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
					'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
					'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
					'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
				}
			}.items() if name == key
		),
		{},
	)

def build_settings(
	user_settings: dict[str, typing.Any],
	wordlist: list[str]
):
	if 'exclude_words' in user_settings:
		for word in user_settings['exclude_words']:
			if (word) and (word in wordlist):
				wordlist.remove(word)
	if 'include_words' in user_settings:
		for word in user_settings['include_words']:
			if (word) and (word not in wordlist):
				wordlist.append(word)
	settings = {
		'all_lowercase': False,
		'allow_repeats': False,
		'display_debug': False,
		'exclude_words': [],
		'ignore_scores': False,
		'include_words': [],
		'letter_scores': '',
		'max_words_len': max(len(word) for word in wordlist),
		'min_words_len': 2,
	} | user_settings
	settings |= {
		'max_words_len': min(
			settings['max_words_len'], max(len(word) for word in wordlist)
		),
		'min_words_len': max(
			settings['min_words_len'], 2
		),
	}
	settings |= {
		'letter_scores': settings['letter_scores']
			if build_letter_scores(settings['letter_scores'])
			else 'quarrel'
	}

	return settings

class Ruleset:
	def __init__(
		self,
		wordlist: typing.Optional[list[str]] = None,
		settings: typing.Optional[typing.Dict[str, typing.Any]] = None
	) -> None:
		if settings is None:
			settings = {}
		if wordlist:
			if 'exclude_words' in settings:
				for word in settings['exclude_words']:
					if (word) and (word in wordlist):
						wordlist.remove(word)
			if 'include_words' in settings:
				for word in settings['include_words']:
					if (word) and (word not in wordlist):
						wordlist.append(word)
		else:
			wordlist = wordlist_full
		settings = build_settings(settings, wordlist)
		try:
			with open(settings['custom_dictionary'], 'r') as f:
				wordlist = f.read().splitlines()
		except (FileNotFoundError, KeyError):
			wordlist = wordlist_full
		wordlist = [
			word for word in wordlist if settings['min_words_len'] <= len(word) <= settings['max_words_len']
		]
		self.settings = settings
		self.scores = {
			word: sum(build_letter_scores(self.settings['letter_scores'])[char] for char in word) for word in sorted(
				sorted(wordlist),
				key=lambda word: (
					len(word), sum(build_letter_scores(self.settings['letter_scores'])[char] for char in word)
				), reverse=True
			)
		}
		self.wordlist = wordlist

	def __getitem__(self, key: str) -> typing.Any:
		if key in self.settings.keys():
			return self.settings[key]
		else:
			raise KeyError(f'{key} not found in settings')

	def get_setting(
		self,
		key: str,
	) -> typing.Union[typing.Any, None]:
		return self.settings[key] if key in self.settings else None

	def get_settings(
		self,
	) -> typing.Dict[str, typing.Any]:
		return self.settings
	
	def get_settings_str(
		self,
	) -> str:
		return json.dumps(self.settings, indent=2, sort_keys=True).replace('  ', '\t') + '\n'

	def solve(
		self,
		query: str,
	) -> dict:
		scores_out = {}

		if self.settings['display_debug']:
			print('')

		for len_iter in range(
			2, max(
				len(word) for word in self.wordlist
			) if self.settings['allow_repeats'] else len(query) + 1
		)[::-1]:
			scores_out |= {len_iter: [[], 0]}
			for word in self.scores:
				query_iter, word_iter = copy.deepcopy(query), copy.deepcopy(word)
				word_fits = False

				if (
					len(word) == len_iter
					if self.settings['ignore_scores']
					else len(word) <= len_iter
				) and set(word) <= set(query):
					if not self.settings['ignore_scores'] and self.scores[word] < scores_out[len_iter][1]:
						continue

					if self.settings['allow_repeats']:
						word_fits = all(char in query for char in word)

					else:
						for char in word:
							query_iter = query_iter.replace(char, ' ', 1)
							word_iter = word_iter.replace(char, ' ', 1)

							if self.settings['display_debug']:
								print(f'input: {[query_iter]} | {[word]}: {[word_iter]}')

						if query_iter.count(' ') == word_iter.count(' ') != 0:
							word_fits = True

					if self.settings['display_debug']:
						print(f'{[word]} fits for {[len_iter]}')

				if word_fits:
					scores_out[len_iter][0].append(word)
					if not self.settings['ignore_scores']:
						scores_out[len_iter][1] = self.scores[scores_out[len_iter][0][0]]

			if self.settings['display_debug']:
				print(f' - output for {[len_iter]}: {scores_out[len_iter][0]}')

		for key, val in copy.deepcopy(scores_out).items():
			with contextlib.suppress(IndexError, KeyError):
				if not val:
					del scores_out[key]
					if self.settings['display_debug']:
						print(f' - removed {[key]} for empty list')
				elif not self.settings['ignore_scores'] and any(
					word in scores_out[key][0] for word in scores_out[key-1][0]
				):
					del scores_out[key]
					if self.settings['display_debug']:
						print(f' - removed {[key]} for duplicate/s')

		return scores_out

	def solve_str(
		self,
		query: str
	):
		scores_out = self.solve(query)
		try:
			if len(scores_out[len(query)][0][0]) != len(query):
				anagram_found = '  \t warning: anagram not found\n\n'
			else:
				anagram_found = ''
		except (IndexError, KeyError):
			anagram_found = ''

		return str(
			f'\n  \t--- query: {query} ({len(query)} letters'
			+ (' + repeats' if self.settings['allow_repeats'] else '') + ') ---\n\n' + (
				(
					anagram_found + '\n\n'.join(
						f'\t{key} letters'
						+ (
							''
							if self.settings['ignore_scores']
							else f' - {scores_out[key][1]} points'
						) + '\n\t ' + ', '.join(
							sorted(
								word if self.settings['all_lowercase'] else word.upper()
								for word in scores_out[key][0]
							)
						)
						for key in scores_out.keys()
						if scores_out[key][0]
					)
				)
				if any(scores_out[key][0] for key in scores_out.keys())
				else '\tno words found'
			)
		)

	def get_wordlist(
		self,
	) -> list[str]:
		return self.wordlist

if __name__ == '__main__':
	print('\n\tloading settings, wordlist, etc...')

	try:
		with open(
			os.path.join(
				sys.path[0], 'settings.json'
			), 'tr'
		) as settings_file:
			settings_import = json.load(settings_file)

	except FileNotFoundError:
		settings_import = {}


	q = Ruleset(
		wordlist=wordlist_full,
		settings=build_settings(settings_import, wordlist_full)
	)

	if q.settings['display_debug']:
		print(q.get_settings())

	open(
		os.path.join(
			sys.path[0], 'settings.json'
		), 'tw'
	).write(
		str(q.get_settings())
	)

	print('\n\t\tdone!')

	while True:
		print('')
		query = ''
		while not (
			q.settings['min_words_length']
			<= len(query)
			<= q.settings['max_words_length']
		) and (
			char not in string.ascii_lowercase for char in query
		):
			query = ''.join(
				sorted(dict.fromkeys(input('> ').lower()))
				if q.settings['allow_repeats']
				else sorted(input('> ').lower())
			)
		print(q.solve_str(query))
