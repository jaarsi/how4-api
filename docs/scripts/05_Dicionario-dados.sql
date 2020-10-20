SELECT  t.table_name,
        c.column_name,
        c.column_type,
        c.column_key,
        c.is_nullable,
        c.extra,
        c.column_comment
FROM information_schema.tables t
INNER JOIN information_schema.columns c ON t.table_name = c.table_name
                                       AND t.table_schema = c.table_schema
WHERE t.table_type IN ('base table', 'view')
  AND t.table_schema LIKE '%db_Mercearia_DES%'
ORDER BY t.table_schema,
         t.table_name,
         c.ordinal_position;
