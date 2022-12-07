from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import datetime

# Create your views here.
from .Export import roundoff, export, business_days


def index(request, *args, **kwargs):  # *args, **kwargs
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", {})


P = ";"
O = "./main/src/SSoT.csv"
e = max
d = all
c = len
J = "date"
Q = float
N = "days"
C = int
H = str
F = "Predecessor"
B = "ID"


def scheduler(df, date_1):
    b = "start"
    X = "nan"
    W = ", "
    S = "end"
    P = "%d-%m-%Y %H:%M"
    G = date_1
    D = df
    K = []
    L = []
    I = []
    M = []
    for (R, A) in D.iterrows():
        if R == 0:
            J = business_days(G, Q(A[N]))
            L += [J]
            K += [G]
            I.append(A[B])
        else:
            E = A[F].split(W)
            if X in E and c(E) != 1:
                E.remove(X)
            T = d((A in I for A in E))
            if T:
                O = []
                E = A[F].split(W)
                for U in E:
                    O.append(D[D[B] == U][S].values)
                V = np.concatenate(O, axis=0)
                C = e(V)
                C = H(C)
                C = datetime.datetime.strptime(C, P)
                if C.hour == 18:
                    C = C + datetime.timedelta(hours=14)
                K += [C]
                J = business_days(C, Q(A[N]))
                L += [J]
                I.append(A[B])
            elif A[F] == X:
                J = business_days(G, Q(A[N]))
                L += [J]
                K += [G]
                I.append(A[B])
            else:
                M += [A[B]]
                K += [G]
                L += [G]
        f = [A.strftime(P) for A in K]
        D[b] = pd.DataFrame({b: f})
        g = [A.strftime(P) for A in L]
        D[S] = pd.DataFrame({S: g})
    Y = 0
    Z = 0
    a = 0
    while c(M) != 0 and Y < 200:
        Y += 1
        for (R, A) in D.iterrows():
            E = A[F].split(W)
            T = d((A in I for A in E))
            if T and A[B] in M:
                O = []
                E = A[F].split(W)
                for U in E:
                    O.append(D[D[B] == U][S].values)
                V = np.concatenate(O, axis=0)
                C = e(V)
                C = H(C)
                C = datetime.datetime.strptime(C, P)
                if C.hour == 18:
                    C = C + datetime.timedelta(hours=14)
                Z = C
                h = business_days(C, Q(A[N]))
                a = h
                I.append(A[B])
                M.remove(A[B])
                D.loc[(R, b)] = Z.strftime(P)
                D.loc[(R, S)] = a.strftime(P)
            elif A[F] == X and A[B] in M:
                J = business_days(G, Q(A[N]))
                L += [J]
                K += [G]
                I.append(A[B])
                M.remove(A[B])
    return D


def customisation(request, *args, **kwargs):
    W = "Standard"
    V = "WQEC01"
    U = "PST03"
    T = "name"
    N = "2"
    I = "C01"
    G = "Worse case"
    D = "Best case"
    Q = request.POST[T]
    R = request.POST[J]
    A = pd.read_csv(O, delimiter=P)
    A = A.astype(H)
    E = request.POST["button9"]
    if E == "SSG":
        A.at[(C(A[A[B] == U].index.values), G)] = "0.5"
        A.at[(C(A[A[B] == V].index.values), G)] = N
    else:
        A.at[(C(A[A[B] == U].index.values), D)] = N
        A.at[(C(A[A[B] == V].index.values), D)] = "7"
    F = request.POST.getlist("BaseQAinput")
    F.append("0")
    if any(("BF" in A for A in F)):
        if E == W:
            A.at[(C(A[A[B] == I].index.values), D)] = "6"
        else:
            A.at[(C(A[A[B] == I].index.values), D)] = N
    elif E == W:
        A.at[(C(A[A[B] == I].index.values), D)] = "4.5"
    else:
        A.at[(C(A[A[B] == I].index.values), D)] = "1.5"
    A = A[A["IncludeOnlyIN"].isin(F)]
    K = []
    for S in range(4):
        K.append(request.POST["button" + H(S + 1)])
    A = A[~A["Activity Selection"].isin(K)]
    for (L, M) in A.iterrows():
        A[D][L] = roundoff(pd.to_numeric(M[D]))
        A[G][L] = roundoff(pd.to_numeric(M[G]))
    A = A.astype(H)
    return render(request, "customisation.html", {"df": A, T: Q, J: R})


def table(request, *args, **kwargs):
    b = "ID1"
    a = "Resources-"
    Z = "left"
    Y = "timeID"
    X = True
    C = request.POST.getlist("box")
    A = pd.read_csv(O, delimiter=P)
    A = A.astype(H)
    Q = A.loc[~A[B].isin(C)]
    for (R, S) in Q.iterrows():
        A[F] = A[F].replace(S[B], A[F][R], regex=X)
    A.drop(A.loc[~A[B].isin(C)].index, inplace=X)
    A = A.reset_index()
    I = []
    K = []
    for L in C:
        K.append(request.POST.get("time-" + L))
        I.append(L)
    D = pd.DataFrame({Y: I, N: K})
    D = D.astype(H)
    A = pd.merge(A, D.rename(columns={Y: B}), on=B, how=Z)
    T = request.POST.get(J)
    U = datetime.datetime.strptime(T + " 08:00", "%m/%d/%Y %H:%M")
    A = scheduler(A, U)
    E = []
    G = []
    for (M, C) in request.POST.lists():
        if M.startswith(a):
            E.append(C)
            G.append(M.replace(a, ""))
    V = pd.DataFrame({b: G, "Resources": E})
    W = pd.merge(A, V.rename(columns={b: B}), on=B, how=Z)
    export(A, G, E)
    return render(request, "table.html", {"table": W.astype(H)})
