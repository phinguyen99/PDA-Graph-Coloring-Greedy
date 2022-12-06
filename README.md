# PDA-Graph-Coloring-Greedy

| Greedy Graph Coloring
1:	begin
2:	Let {v0, v1,…, vn-1} be a sequence of the vertices in V
3:	Let vi .adjacent[ ] be list of adjacent vertices 
4:	Let result[-1;-1;…;-1 ] be list colors of each vertex
5:	Let available[F;F;…;F ] be list to check if a vertex is colored yet?
6:	v0 .color ← 0, result[0] ← 0
7:	     for vi:=v1 to vn-1 
8:	   for adj in vi.adjacent[ ]
9:
10	      if result[adj] <> -1 then available[result[adj]] ← True end if
end for
11:	     for mark:=0 to n-1
12:
13:	if available[mark] = False then break end if
    end for
14:	    vi .color ← mark, result[i] ← mark
15:	for adj in vi.adjacent[ ]
16:
17:
18:
19:	if result[adj] <> -1 then available[result[adj]] ← False end if
    end for
end for
end
