LEAGUE:=test

default:
	sed -i "/DEFAULT_LEAGUE/s/'.*'/'${DEFAULT}'/g" constants.py

table:
	python3 elo/table.py --league ${LEAGUE}
