# {}	TRUE
# {}(){}	TRUE
# ()[[Extra Characters]]	TRUE
# (){}[[]]	TRUE
# {}{Code}[Fellows](())	TRUE
# [({}]	FALSE
# (](	FALSE
# {(})	FALSE

# {	FALSE	error unmatched opening { remaining.
# )	FALSE	error closing ) arrived without corresponding opening.
# [}	FALSE	error closing }. Doesn’t match opening (.