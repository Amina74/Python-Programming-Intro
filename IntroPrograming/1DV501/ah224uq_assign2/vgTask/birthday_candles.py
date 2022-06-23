canboxs, candles, sumboxs, box, = 24, 0, 0, 0

for year in range(101):
    while True:
        if candles < year:
            box += 1
            candles += canboxs
        else:
            break
    sumboxs += box

    candles -= year

    if box != 0:
        print(f'Before birthday, {str(year)} buy {str(box)} box(es)')
    box = 0

print('Total number of boxes:' + " " + str(sumboxs) + " "
      + ' Remaining candles:' + " " + str(candles))
