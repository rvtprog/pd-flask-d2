# Pārbaudes darbs Flask

### Uzdevums 1
Izveidot route /calc, kas saņem JSON, kurš atbilst šādam formātam:
``` json
{
    "sk1":"10",
    "sk2":"5",
    "darb":"+"
}
```
- sk1 un sk2 => Veseli skaitļi
- darb => Iespējamās darbības (+, -, /, *)

Uz šādu pieprasījumu jāatbild ar:
``` json
{
    "rez":"15"
}
```