import segno
employees=[
    '刘备',
    '张飞',
    '关羽',
    '吕布'
]
with open('employees.txt','w') as f:
    for emp in employees:
        f.write(f'{emp}\n')
        qr = segno.make(emp, encoding='utf-8',micro=False)
        qr.save(f'{emp}.png', scale=10)