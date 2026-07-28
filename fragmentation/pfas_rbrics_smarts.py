# PFAS-rBRICS SMARTS Additions

PFAS_ENVIRONS = {

    #Fluorinated carbon environments
    "L24": "[C;!R;X4;$([C](F)([*])([#6]))]",
    "L25": "[C;X4;$([C](F)([*])([#6]))]",
    "L24p": "[C;!R;X4;H0;$([C](F)([*])([#6]))]",
    "L24e": "[C;!R;X4;H0;$([C](F)(*)(O))]",

    #Non-fluorinated carbon
    "L4nf": "[C;!R;X4;!$([C](F))]",

    #Aromatic/carbon environments
    "L26":"[a]",
    "L27":"[C;!R;X4]",
    "L27r":"[C;X4;R]",
    "L29":"[C;!R;X3;$(C(=[#6]))]",

    # Oxygen/nitrogen
    "L28O":"[O;D2;!$([O-]);!R]-[#6]",
    "L28N":"[N;D3;!R;!$([N]-C(=O))]-[#6]",

    # Sulfur chemistry
    "L12x":"[S;!R;D3]",
    "L12pfsa":"[S;X4](=O)(=O)",
    "L5s":"[N;!R;$([N]-[S](=O)(=O))]",

    # Silicon support
    "L60":"[Si;X4]",
    "L61":"[O;D2;!$([O-])]",
}

PFAS_COMPATS = (

    #PFCA headgroup
    (("24p", "6", "-"),),

    #Fluorotelomer boundary
    (("24p", "4nf", "-"),
     ("4nf", "24p", "-")),

    #Aromatic-alkyl linker
    (("26", "27", "-"),),

    #O/N to alkyl
    (("28O", "27", "-"),
     ("28N", "27", "-")),

    #O/N to carbonyl
    (("28O", "6", "-"),
     ("28N", "6", "-")),

    #Ether/amine to PFAS tail
    (("28O", "24p", "-"),
     ("24p", "28O", "-")),

    (("28N", "24p", "-"),
     ("24p", "28N", "-")),

    #Perfluoroether support
    (("28O", "24e", "-"),
     ("24e", "28O", "-")),

    #Fluorotelomer CH2-O/N boundaries
    (("4nf", "28O", "-"),
     ("4nf", "28N", "-")),

    (("27", "28O", "-"),
     ("27", "28N", "-")),

    #Sulfur-imide/sulfoxide support
    (("26", "12x", "-"),),

    (("12x", "28O", "-"),
     ("12x", "28N", "-")),

    (("24p", "12x", "-"),),

    #PFSA support
    (("24p", "12pfsa", "-"),),
    (("24e", "12pfsa", "-"),),
    (("12pfsa", "5s", "-"),),
    (("5s", "27", "-"),),
    (("12pfsa", "28O", "-"),),
    (("12pfsa", "28N", "-"),),

    #Ring sulfone cleavage
    (("12", "27r", "-;@"),),

    #Aromatic, exocyclic sp2 carbon
    (("26", "29", "-"),),

    #Silicon-containing PFAS
    (("61", "60", "-"),),
    (("60", "24p", "-"),),
    (("60", "24e", "-"),),
    (("26", "60", "-"),),
    (("60", "27", "-"),),
)
