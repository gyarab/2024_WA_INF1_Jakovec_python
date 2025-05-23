# Databáze punku

Vítejte v dokumentaci databáze punku. Tato databáze slouží k ukládání informací o punkových skupinách, albech, písních a dalších souvisejících údajích.

## Struktura databáze

Databáze je organizována do několika tabulek, které obsahují informace o jednotlivých entitách. Následující tabulky jsou součástí databáze:

1. Skupiny - obsahuje informace o punkových skupinách, jako je název, země původu, žánr atd.
2. Alba - obsahuje informace o albech, včetně názvu, roku vydání, seznamu skladeb atd.
3. Písně - obsahuje odkazy (existují-li) na stránku s akordy a textem písně

## Použití databáze

Pro práci s databází punku můžete použít SQL dotazy. Zde je příklad jednoduchého dotazu, který vrátí všechny punkové skupiny:

```sql
SELECT * FROM bands;
```

## Další informace

Pro podrobnější informace o použití databáze a dostupných funkcionalitách kontaktujte autora.
