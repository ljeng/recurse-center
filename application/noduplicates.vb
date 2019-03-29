Option Explicit
Function NODUPLICATES(Rng As Range, Low As Integer, High As Integer)
    Dim i, j, Random(), As Integer, Found As Boolean, Cell As Range
    ReDim Random(Low To High)
    i = Low
    For j = Low To High
        Found = False
        For Each Cell In Rng
            If j = Cell.Value Then
                Found = True
            End If
        Next Cell
        If Found = False Then
            Random(i) = j
            i = i + 1
        End If
    Next j
    ReDim Preserve Random(LBound(Random) To UBound(Random) - High + i - 1)
    NODUPLICATES = Application.WorksheetFunction.Index(Random, Application.WorksheetFunction.RandBetween(LBound(Random), UBound(Random)))
End Function
