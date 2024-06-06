from translate import translate


texts = ['''The mod &9Construction Wand&r adds helpful wands that are used when building. \\n \\n When right-clicking a face of a block with the wand, it will extend that face out as long as you have the blocks in your inventory.''',
         '''To \\\"unmount\\\" the blocks from the Minecart, simply turn off the redstone signal and let the Minecart ride through.''',
         '''On one of the faces, we'll want to put a Logic Adapter down, then skip a block above it and then place another Adapter. Set the top Adapter to &9\\\"Activation\\\"&r, and the bottom Adapter to &c\\\"Damage Critical\\\"&r.''']


for text in texts:
    a = translate(text)
    print(a)
