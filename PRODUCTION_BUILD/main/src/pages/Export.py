import math
import datetime
import pandas as pd
import numpy as np

A3 = range
f = len
K = str
J = int


def business_days(fd, ad):
    B = ad * 10
    A = fd
    while B > 0:
        A += datetime.timedelta(hours=1)
        D = A.weekday()
        C = A.hour
        if C > 18 or C <= 8 or D >= 5:
            continue
        B -= 1
    return A


def roundoff(x):
    return J(math.ceil(x / 0.5)) * 0.5


def export(df, indexs, res):
    AR = "code1"
    AQ = "100%"
    AP = "CCST"
    AO = "External"
    AN = "SSG"
    AM = "Task Mode"
    AL = "Active"
    A2 = False
    A1 = "Outline Level"
    A0 = "Name"
    u = "Resources"
    t = "Work"
    s = "MS"
    r = "Finish"
    q = "Auto Scheduled"
    p = "Yes"
    e = "outline"
    d = "start"
    c = "ID"
    a = ""
    V = "sorting"
    U = "Duration"
    T = "code"
    Q = True
    P = "%d-%m-%Y %H:%M"
    G = "Predecessor"
    C = df
    B = "nan"
    g = [p] * J(C.shape[0])
    h = [q] * J(C.shape[0])
    A = pd.DataFrame({AL: g, AM: h})
    A[A0] = C["Title"] + " (" + C[c] + ")"
    A[T] = C[c]
    A[U] = C["days"]
    A[d] = C[d]
    A[r] = C["end"]
    for (L, D) in C.iterrows():
        i = D[G]
        j = i.split(", ")
        j = [A for A in j if K(A) != B]
        W = np.unique(j)
        W = ";".join(W)
        C[G][L] = W
    A[G] = C[G]
    A[V] = C[V]
    A[e] = C[e]
    M = A[V].unique()
    for R in M:
        if R != "1" and R != "24" and R != "33" and R != "39":
            k = A[d][A[V] == R]
            l = A[r][A[V] == R]
            X = []
            Y = []
            for m in k:
                X.append(datetime.datetime.strptime(m, P))
            for n in l:
                Y.append(datetime.datetime.strptime(n, P))
            I = min(X)
            N = max(Y)
            N = N.strftime(P)
            I = I.strftime(P)
            A = A.sort_index().reset_index(drop=Q)
    S = []
    A4 = []
    A5 = []
    M = []
    g = [p] * J(f(S))
    A6 = [B] * J(f(S))
    h = [q] * J(f(S))
    H = pd.DataFrame({AL: g, AM: h, A0: A4, T: A5, U: M, d: S, r: S, G: A6})
    A7 = [3] * J(f(S))
    H[e] = pd.DataFrame({e: A7})
    M = A[V].unique()
    M = M[M != B]
    AS = []
    AT = []
    k = A[d]
    l = A[r]
    X = []
    Y = []
    for m in k:
        X.append(datetime.datetime.strptime(m, P))
    for n in l:
        Y.append(datetime.datetime.strptime(n, P))
    I = min(X)
    N = max(Y)
    A8 = N - I
    N = N.strftime(P)
    I = I.strftime(P)
    H = H.sort_index().reset_index(drop=Q)
    for (L, D) in H.iterrows():
        if D[G].find(B) == -1:
            i = D[G]
            W = ";".join(i)
            H[G][L] = W

    E = H.append(A)
    o = A3(1, E.shape[0] + 1)
    E.insert(loc=0, column=c, value=o)
    E = E.drop(columns=[V])
    E = E.reset_index(drop=Q)
    E = E.applymap(K)
    v = []
    w = []
    x = []
    y = []
    z = []
    o = A3(1, 11)
    A9 = [s, "EE", "AE", AN, s, AO, "PM", "CM", "BI", AP]
    AA = [s, "EE", "AE", AN, s, AO, "PM", "CM", "BI", AP]
    AB = [t] * 10
    AC = [B] * 10
    AD = [B] * 10
    AE = [B] * 10
    AF = [B] * 10
    AG = [AQ] * 10
    AH = ["kr. 0,00/t"] * 10
    AI = [0] * 10
    Z = pd.DataFrame(
        {
            c: o,
            "Names": A9,
            "Initials": AA,
            "Type": AB,
            "Material Label": AC,
            "Group": AD,
            "Email Address": AE,
            "User Logon Account": AF,
            "Max Units": AG,
            "Standard Rate": AH,
            "Cost Per Use": AI,
        }
    )
    AJ = pd.DataFrame({AR: indexs, u: res})
    E = pd.merge(E, AJ.rename(columns={AR: T}), on=T, how="left")
    for (L, D) in E.iterrows():
        if K(D[u]) != B:
            for AK in D[u]:
                v.append(D[A0])
                w.append(AK)
                x.append("0")
                y.append(J(pd.to_numeric(D[U], downcast="float") * 10))
                z.append(AQ)
    O = pd.DataFrame(
        {"Task Name": v, "Resource Name": w, "% Work Complete": x, t: y, "Units": z}
    )
    F = E.drop(columns=[u, T])
    F = F.applymap(K)
    for (L, D) in F.iterrows():
        F[U][L] = D[U].replace(".", ",")
    F[U] = F[U] + " days"
    F = F.rename({e: A1}, axis=1)
    F["Notes"] = [B] * F.shape[0]
    F[A1] = pd.to_numeric(F[A1])
    Z = Z.applymap(K)
    O = O.applymap(K)
    O[t] = O[t] + "h"
    F = F.replace(B, a)
    Z = Z.replace(B, a)
    O = O.replace(B, a)
    b = pd.ExcelWriter(
        "TimePlan.xlsx",
        engine="xlsxwriter",
        datetime_format="mmm d yyyy hh:mm:ss",
        date_format="mmmm dd yyyy",
    )
    F[G].replace(np.nan,"")
    F.to_excel(b, sheet_name="Plan", index=A2, header=Q, na_rep=a)
    Z.to_excel(b, sheet_name="Resource", index=A2, header=Q, na_rep=a)
    O.to_excel(b, sheet_name="Assignment", index=A2, header=Q, na_rep=a)
    b.save()
