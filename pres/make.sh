TEMPLATE=index.html.template

CONTENT=""

for d in content/* ; do
	CONTENT+="<section>\n"
	for f in ${d}/* ; do
		f_content=`cat $f`
		raw="<section data-markdown>\n${f_content}\n</section>\n"
		CONTENT+=${raw/##/\#\#}
		echo $CONTENT
		sed -e "s@{{{TO_REPLACE}}}@${CONTENT}@" $TEMPLATE
	done
	CONTENT+="</section>\n"
done


sed -e "s@{{{TO_REPLACE}}}@${CONTENT}@" $TEMPLATE > index.html

