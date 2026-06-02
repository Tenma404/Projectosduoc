alumno={
"nombre": "John Kennedy",
"edad ": 30,
"nacionalidad ":  "chilena"
}

print (alumno)
print (alumno["edad "])

alumno["Email"]="emailfalso@asdf.com"


print (alumno)

alumno["nacionalidad "]="Gringa"

del alumno["edad "]

print (alumno)