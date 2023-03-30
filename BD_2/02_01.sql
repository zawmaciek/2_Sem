USE [BD2_1a_2023z]
GO
DECLARE crs_cwiczenia CURSOR STATIC FOR SELECT IDproduktu, NazwaProduktu, CenaJednostkowa FROM Produkty;
OPEN crs_cwiczenia;
BEGIN
	DECLARE @counter INT;
	SET @counter=1;
	FETCH NEXT FROM crs_cwiczenia
	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @counter=@counter+1;
		IF @counter%10=0  
		  PRINT CONCAT('jestesmy w ',@counter,' wierszu')
		FETCH NEXT FROM crs_cwiczenia
	END
END
CLOSE crs_cwiczenia;
DEALLOCATE crs_cwiczenia;
