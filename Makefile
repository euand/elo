LEAGUE:=test

default:
	sed -i "/DEFAULT_LEAGUE/s/'.*'/'${DEFAULT}'/g" elo/constants.py

table:
	python3 elo/table.py --league ${LEAGUE}

add-matches:
	python3 app/gui.py
