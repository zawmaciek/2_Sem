USE [BD2_1a_2023z]
GO
DROP TABLE IF EXISTS Kopia_Pracownicy;
SELECT * INTO Kopia_Pracownicy FROM Pracownicy;
ALTER TABLE Kopia_Pracownicy DROP COLUMN Fotografia;
DROP TABLE IF EXISTS ##Zmiany_Kopia_Pracownicy;
SELECT * INTO ##Zmiany_Kopia_Pracownicy FROM Kopia_Pracownicy WHERE 1=2;
ALTER TABLE ##Zmiany_Kopia_Pracownicy ADD Status_Zmiany VARCHAR(15);
ALTER TABLE ##Zmiany_Kopia_Pracownicy ADD DataZmiany DATETIME;
GO
CREATE TRIGGER Zmiana_Pracownicy 
ON Kopia_Pracownicy
AFTER INSERT,UPDATE,DELETE
AS 
    IF EXISTS(SELECT * FROM inserted) AND EXISTS(SELECT * FROM deleted)
		BEGIN
		INSERT INTO ##Zmiany_Kopia_Pracownicy SELECT *,'updated',GETDATE() FROM deleted;
		END
    ELSE IF EXISTS(SELECT * FROM inserted)
		INSERT INTO ##Zmiany_Kopia_Pracownicy SELECT *,'inserted',GETDATE() FROM inserted;
	ELSE IF EXISTS(SELECT * FROM deleted)
		INSERT INTO ##Zmiany_Kopia_Pracownicy SELECT *,'deleted',GETDATE() FROM deleted;
GO
SELECT * FROM ##Zmiany_Kopia_Pracownicy;


UPDATE Kopia_Pracownicy SET DataZwolnienia=NULL WHERE DataZwolnienia IS NOT NULL;
DELETE FROM Kopia_Pracownicy WHERE P³eæ='k'
INSERT INTO Kopia_Pracownicy VALUES (100,'zawadzki','maciej','m','przedstawiciel handlowy',10,'1999-05-11',GETDATE(),NULL,'aktywny','adres','Bielsko','WA',43392,'USA','(63)345-32145','brak','mr');
GO
SELECT * FROM ##Zmiany_Kopia_Pracownicy;