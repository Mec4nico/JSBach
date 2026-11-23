#!/bin/bash


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html>"
echo "<head>"
echo "    <meta charset="utf-8">"
echo "    <title>Hola món CGI</title>"

cat ../utils/styles.css

echo "</head>"
echo "<body>"

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')

case $comand in	
    	iniciar|aturar|estat)
    		echo "<h2>WAN $comand </h2>"
		echo "<pre>$(echo "wan $comand"|nc 127.0.0.1 1234)</pre>"
		;;
	configurar)
		opcio=$(echo "$QUERY_STRING" | sed -n 's/^.*opcio=\([^&]*\).*$/\1/p')		
		case $opcio in			
			guardar)
				mode=$(echo "$QUERY_STRING" | sed -n 's/^.*mode=\([^&]*\).*$/\1/p')
				int=$(echo "$QUERY_STRING" | sed -n 's/^.*int=\([^&]*\).*$/\1/p')
				if [[ "$mode" == "manual" ]]; then
				    ip=$(echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p')
				    masc=$(echo "$QUERY_STRING" | sed -n 's/^.*masc=\([^&]*\).*$/\1/p')
				    pe=$(echo "$QUERY_STRING" | sed -n 's/^.*pe=\([^&]*\).*$/\1/p')
				    dns=$(echo "$QUERY_STRING" | sed -n 's/^.*dns=\([^&]*\).*$/\1/p')
				fi
				echo "wan $comand $opcio $mode $int $ip $masc $pe $dns"
				echo "$(echo "wan $comand $opcio $mode $int $ip $masc $pe $dns"|nc 127.0.0.1 1234)"
			;;
		esac
		;;
esac

echo "</body>"
echo "</html>"
