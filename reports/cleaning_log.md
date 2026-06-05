\# Polyhouse Sensor Data Cleaning Log



\## Dataset Summary



Rows Before Cleaning: 52



Rows After Cleaning: 52



Columns: 8



\---



\## Missing Value Audit



| Column | Nulls Before | Nulls After |

|----------|----------:|----------:|

| timestamp | 0 | 0 |

| temperature | 5 | 0 |

| humidity | 3 | 0 |

| soil\_moisture | 5 | 0 |

| co2 | 5 | 0 |

| light\_intensity | 5 | 0 |

| zone | 3 | 0 |

| source\_file | 0 | 0 |



\---



\## Cleaning Decisions



\### temperature



Method:

Linear Interpolation



Agritech Rationale:

Temperature inside a polyhouse changes gradually over time. Interpolation preserves realistic environmental trends during short sensor outages.



\---



\### humidity



Method:

Linear Interpolation



Agritech Rationale:

Humidity values are continuous environmental measurements. Interpolation maintains temporal consistency.



\---



\### soil\_moisture



Method:

Linear Interpolation



Agritech Rationale:

Soil moisture generally changes progressively due to irrigation and plant uptake. Interpolation is appropriate for small missing gaps.



\---



\### co2



Method:

Linear Interpolation



Agritech Rationale:

CO₂ concentration fluctuates gradually under normal greenhouse conditions. Interpolation avoids artificial spikes.



\---



\### light\_intensity



Method:

Linear Interpolation



Agritech Rationale:

Light intensity follows predictable daily patterns. Interpolation preserves continuity of sunlight exposure data.



\---



\### zone



Method:

Mode Imputation



Agritech Rationale:

Zone is a categorical field identifying greenhouse sections. Missing values were filled with the most frequent zone.



\---



\### timestamp



Method:

No Imputation Required



Agritech Rationale:

No missing timestamps were present.



\---



\### source\_file



Method:

No Imputation Required



Agritech Rationale:

Metadata column used for data lineage and traceability.



\---



\## Output Files



Generated:



\- data/processed/02\_cleaned.parquet

\- data/processed/sample\_cleaned\_50\_rows.csv



Cleaning completed successfully.

