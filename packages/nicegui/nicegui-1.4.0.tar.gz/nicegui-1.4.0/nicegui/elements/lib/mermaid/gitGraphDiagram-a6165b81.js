import { c as O, s as vt, g as At, a as Ot, b as St, B as It, D as Gt, l as G, f as D, E as Pt, H as Ht, I as ut, j as Nt, z as Bt, J as Vt } from "./mermaid-5f2d2ec5.js";
var mt = function() {
  var r = function(q, h, b, k) {
    for (b = b || {}, k = q.length; k--; b[q[k]] = h)
      ;
    return b;
  }, a = [1, 3], o = [1, 6], u = [1, 4], n = [1, 5], c = [2, 5], m = [1, 12], l = [5, 7, 13, 19, 21, 23, 24, 26, 28, 31, 36, 39, 46], E = [7, 13, 19, 21, 23, 24, 26, 28, 31, 36, 39], _ = [7, 12, 13, 19, 21, 23, 24, 26, 28, 31, 36, 39], i = [7, 13, 46], g = [1, 42], f = [1, 41], x = [7, 13, 29, 32, 34, 37, 46], p = [1, 55], d = [1, 56], y = [1, 57], N = [7, 13, 32, 34, 41, 46], w = {
    trace: function() {
    },
    yy: {},
    symbols_: { error: 2, start: 3, eol: 4, GG: 5, document: 6, EOF: 7, ":": 8, DIR: 9, options: 10, body: 11, OPT: 12, NL: 13, line: 14, statement: 15, commitStatement: 16, mergeStatement: 17, cherryPickStatement: 18, acc_title: 19, acc_title_value: 20, acc_descr: 21, acc_descr_value: 22, acc_descr_multiline_value: 23, section: 24, branchStatement: 25, CHECKOUT: 26, ref: 27, BRANCH: 28, ORDER: 29, NUM: 30, CHERRY_PICK: 31, COMMIT_ID: 32, STR: 33, COMMIT_TAG: 34, EMPTYSTR: 35, MERGE: 36, COMMIT_TYPE: 37, commitType: 38, COMMIT: 39, commit_arg: 40, COMMIT_MSG: 41, NORMAL: 42, REVERSE: 43, HIGHLIGHT: 44, ID: 45, ";": 46, $accept: 0, $end: 1 },
    terminals_: { 2: "error", 5: "GG", 7: "EOF", 8: ":", 9: "DIR", 12: "OPT", 13: "NL", 19: "acc_title", 20: "acc_title_value", 21: "acc_descr", 22: "acc_descr_value", 23: "acc_descr_multiline_value", 24: "section", 26: "CHECKOUT", 28: "BRANCH", 29: "ORDER", 30: "NUM", 31: "CHERRY_PICK", 32: "COMMIT_ID", 33: "STR", 34: "COMMIT_TAG", 35: "EMPTYSTR", 36: "MERGE", 37: "COMMIT_TYPE", 39: "COMMIT", 41: "COMMIT_MSG", 42: "NORMAL", 43: "REVERSE", 44: "HIGHLIGHT", 45: "ID", 46: ";" },
    productions_: [0, [3, 2], [3, 3], [3, 4], [3, 5], [6, 0], [6, 2], [10, 2], [10, 1], [11, 0], [11, 2], [14, 2], [14, 1], [15, 1], [15, 1], [15, 1], [15, 2], [15, 2], [15, 1], [15, 1], [15, 1], [15, 2], [25, 2], [25, 4], [18, 3], [18, 5], [18, 5], [18, 5], [18, 5], [17, 2], [17, 4], [17, 4], [17, 4], [17, 6], [17, 6], [17, 6], [17, 6], [17, 6], [17, 6], [17, 8], [17, 8], [17, 8], [17, 8], [17, 8], [17, 8], [16, 2], [16, 3], [16, 3], [16, 5], [16, 5], [16, 3], [16, 5], [16, 5], [16, 5], [16, 5], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 3], [16, 5], [16, 5], [16, 5], [16, 5], [16, 5], [16, 5], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 7], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [16, 9], [40, 0], [40, 1], [38, 1], [38, 1], [38, 1], [27, 1], [27, 1], [4, 1], [4, 1], [4, 1]],
    performAction: function(h, b, k, s, T, t, W) {
      var e = t.length - 1;
      switch (T) {
        case 2:
          return t[e];
        case 3:
          return t[e - 1];
        case 4:
          return s.setDirection(t[e - 3]), t[e - 1];
        case 6:
          s.setOptions(t[e - 1]), this.$ = t[e];
          break;
        case 7:
          t[e - 1] += t[e], this.$ = t[e - 1];
          break;
        case 9:
          this.$ = [];
          break;
        case 10:
          t[e - 1].push(t[e]), this.$ = t[e - 1];
          break;
        case 11:
          this.$ = t[e - 1];
          break;
        case 16:
          this.$ = t[e].trim(), s.setAccTitle(this.$);
          break;
        case 17:
        case 18:
          this.$ = t[e].trim(), s.setAccDescription(this.$);
          break;
        case 19:
          s.addSection(t[e].substr(8)), this.$ = t[e].substr(8);
          break;
        case 21:
          s.checkout(t[e]);
          break;
        case 22:
          s.branch(t[e]);
          break;
        case 23:
          s.branch(t[e - 2], t[e]);
          break;
        case 24:
          s.cherryPick(t[e], "", void 0);
          break;
        case 25:
          s.cherryPick(t[e - 2], "", t[e]);
          break;
        case 26:
        case 28:
          s.cherryPick(t[e - 2], "", "");
          break;
        case 27:
          s.cherryPick(t[e], "", t[e - 2]);
          break;
        case 29:
          s.merge(t[e], "", "", "");
          break;
        case 30:
          s.merge(t[e - 2], t[e], "", "");
          break;
        case 31:
          s.merge(t[e - 2], "", t[e], "");
          break;
        case 32:
          s.merge(t[e - 2], "", "", t[e]);
          break;
        case 33:
          s.merge(t[e - 4], t[e], "", t[e - 2]);
          break;
        case 34:
          s.merge(t[e - 4], "", t[e], t[e - 2]);
          break;
        case 35:
          s.merge(t[e - 4], "", t[e - 2], t[e]);
          break;
        case 36:
          s.merge(t[e - 4], t[e - 2], t[e], "");
          break;
        case 37:
          s.merge(t[e - 4], t[e - 2], "", t[e]);
          break;
        case 38:
          s.merge(t[e - 4], t[e], t[e - 2], "");
          break;
        case 39:
          s.merge(t[e - 6], t[e - 4], t[e - 2], t[e]);
          break;
        case 40:
          s.merge(t[e - 6], t[e], t[e - 4], t[e - 2]);
          break;
        case 41:
          s.merge(t[e - 6], t[e - 4], t[e], t[e - 2]);
          break;
        case 42:
          s.merge(t[e - 6], t[e - 2], t[e - 4], t[e]);
          break;
        case 43:
          s.merge(t[e - 6], t[e], t[e - 2], t[e - 4]);
          break;
        case 44:
          s.merge(t[e - 6], t[e - 2], t[e], t[e - 4]);
          break;
        case 45:
          s.commit(t[e]);
          break;
        case 46:
          s.commit("", "", s.commitType.NORMAL, t[e]);
          break;
        case 47:
          s.commit("", "", t[e], "");
          break;
        case 48:
          s.commit("", "", t[e], t[e - 2]);
          break;
        case 49:
          s.commit("", "", t[e - 2], t[e]);
          break;
        case 50:
          s.commit("", t[e], s.commitType.NORMAL, "");
          break;
        case 51:
          s.commit("", t[e - 2], s.commitType.NORMAL, t[e]);
          break;
        case 52:
          s.commit("", t[e], s.commitType.NORMAL, t[e - 2]);
          break;
        case 53:
          s.commit("", t[e - 2], t[e], "");
          break;
        case 54:
          s.commit("", t[e], t[e - 2], "");
          break;
        case 55:
          s.commit("", t[e - 4], t[e - 2], t[e]);
          break;
        case 56:
          s.commit("", t[e - 4], t[e], t[e - 2]);
          break;
        case 57:
          s.commit("", t[e - 2], t[e - 4], t[e]);
          break;
        case 58:
          s.commit("", t[e], t[e - 4], t[e - 2]);
          break;
        case 59:
          s.commit("", t[e], t[e - 2], t[e - 4]);
          break;
        case 60:
          s.commit("", t[e - 2], t[e], t[e - 4]);
          break;
        case 61:
          s.commit(t[e], "", s.commitType.NORMAL, "");
          break;
        case 62:
          s.commit(t[e], "", s.commitType.NORMAL, t[e - 2]);
          break;
        case 63:
          s.commit(t[e - 2], "", s.commitType.NORMAL, t[e]);
          break;
        case 64:
          s.commit(t[e - 2], "", t[e], "");
          break;
        case 65:
          s.commit(t[e], "", t[e - 2], "");
          break;
        case 66:
          s.commit(t[e], t[e - 2], s.commitType.NORMAL, "");
          break;
        case 67:
          s.commit(t[e - 2], t[e], s.commitType.NORMAL, "");
          break;
        case 68:
          s.commit(t[e - 4], "", t[e - 2], t[e]);
          break;
        case 69:
          s.commit(t[e - 4], "", t[e], t[e - 2]);
          break;
        case 70:
          s.commit(t[e - 2], "", t[e - 4], t[e]);
          break;
        case 71:
          s.commit(t[e], "", t[e - 4], t[e - 2]);
          break;
        case 72:
          s.commit(t[e], "", t[e - 2], t[e - 4]);
          break;
        case 73:
          s.commit(t[e - 2], "", t[e], t[e - 4]);
          break;
        case 74:
          s.commit(t[e - 4], t[e], t[e - 2], "");
          break;
        case 75:
          s.commit(t[e - 4], t[e - 2], t[e], "");
          break;
        case 76:
          s.commit(t[e - 2], t[e], t[e - 4], "");
          break;
        case 77:
          s.commit(t[e], t[e - 2], t[e - 4], "");
          break;
        case 78:
          s.commit(t[e], t[e - 4], t[e - 2], "");
          break;
        case 79:
          s.commit(t[e - 2], t[e - 4], t[e], "");
          break;
        case 80:
          s.commit(t[e - 4], t[e], s.commitType.NORMAL, t[e - 2]);
          break;
        case 81:
          s.commit(t[e - 4], t[e - 2], s.commitType.NORMAL, t[e]);
          break;
        case 82:
          s.commit(t[e - 2], t[e], s.commitType.NORMAL, t[e - 4]);
          break;
        case 83:
          s.commit(t[e], t[e - 2], s.commitType.NORMAL, t[e - 4]);
          break;
        case 84:
          s.commit(t[e], t[e - 4], s.commitType.NORMAL, t[e - 2]);
          break;
        case 85:
          s.commit(t[e - 2], t[e - 4], s.commitType.NORMAL, t[e]);
          break;
        case 86:
          s.commit(t[e - 6], t[e - 4], t[e - 2], t[e]);
          break;
        case 87:
          s.commit(t[e - 6], t[e - 4], t[e], t[e - 2]);
          break;
        case 88:
          s.commit(t[e - 6], t[e - 2], t[e - 4], t[e]);
          break;
        case 89:
          s.commit(t[e - 6], t[e], t[e - 4], t[e - 2]);
          break;
        case 90:
          s.commit(t[e - 6], t[e - 2], t[e], t[e - 4]);
          break;
        case 91:
          s.commit(t[e - 6], t[e], t[e - 2], t[e - 4]);
          break;
        case 92:
          s.commit(t[e - 4], t[e - 6], t[e - 2], t[e]);
          break;
        case 93:
          s.commit(t[e - 4], t[e - 6], t[e], t[e - 2]);
          break;
        case 94:
          s.commit(t[e - 2], t[e - 6], t[e - 4], t[e]);
          break;
        case 95:
          s.commit(t[e], t[e - 6], t[e - 4], t[e - 2]);
          break;
        case 96:
          s.commit(t[e - 2], t[e - 6], t[e], t[e - 4]);
          break;
        case 97:
          s.commit(t[e], t[e - 6], t[e - 2], t[e - 4]);
          break;
        case 98:
          s.commit(t[e], t[e - 4], t[e - 2], t[e - 6]);
          break;
        case 99:
          s.commit(t[e - 2], t[e - 4], t[e], t[e - 6]);
          break;
        case 100:
          s.commit(t[e], t[e - 2], t[e - 4], t[e - 6]);
          break;
        case 101:
          s.commit(t[e - 2], t[e], t[e - 4], t[e - 6]);
          break;
        case 102:
          s.commit(t[e - 4], t[e - 2], t[e], t[e - 6]);
          break;
        case 103:
          s.commit(t[e - 4], t[e], t[e - 2], t[e - 6]);
          break;
        case 104:
          s.commit(t[e - 2], t[e - 4], t[e - 6], t[e]);
          break;
        case 105:
          s.commit(t[e], t[e - 4], t[e - 6], t[e - 2]);
          break;
        case 106:
          s.commit(t[e - 2], t[e], t[e - 6], t[e - 4]);
          break;
        case 107:
          s.commit(t[e], t[e - 2], t[e - 6], t[e - 4]);
          break;
        case 108:
          s.commit(t[e - 4], t[e - 2], t[e - 6], t[e]);
          break;
        case 109:
          s.commit(t[e - 4], t[e], t[e - 6], t[e - 2]);
          break;
        case 110:
          this.$ = "";
          break;
        case 111:
          this.$ = t[e];
          break;
        case 112:
          this.$ = s.commitType.NORMAL;
          break;
        case 113:
          this.$ = s.commitType.REVERSE;
          break;
        case 114:
          this.$ = s.commitType.HIGHLIGHT;
          break;
      }
    },
    table: [{ 3: 1, 4: 2, 5: a, 7: o, 13: u, 46: n }, { 1: [3] }, { 3: 7, 4: 2, 5: a, 7: o, 13: u, 46: n }, { 6: 8, 7: c, 8: [1, 9], 9: [1, 10], 10: 11, 13: m }, r(l, [2, 117]), r(l, [2, 118]), r(l, [2, 119]), { 1: [2, 1] }, { 7: [1, 13] }, { 6: 14, 7: c, 10: 11, 13: m }, { 8: [1, 15] }, r(E, [2, 9], { 11: 16, 12: [1, 17] }), r(_, [2, 8]), { 1: [2, 2] }, { 7: [1, 18] }, { 6: 19, 7: c, 10: 11, 13: m }, { 7: [2, 6], 13: [1, 22], 14: 20, 15: 21, 16: 23, 17: 24, 18: 25, 19: [1, 26], 21: [1, 27], 23: [1, 28], 24: [1, 29], 25: 30, 26: [1, 31], 28: [1, 35], 31: [1, 34], 36: [1, 33], 39: [1, 32] }, r(_, [2, 7]), { 1: [2, 3] }, { 7: [1, 36] }, r(E, [2, 10]), { 4: 37, 7: o, 13: u, 46: n }, r(E, [2, 12]), r(i, [2, 13]), r(i, [2, 14]), r(i, [2, 15]), { 20: [1, 38] }, { 22: [1, 39] }, r(i, [2, 18]), r(i, [2, 19]), r(i, [2, 20]), { 27: 40, 33: g, 45: f }, r(i, [2, 110], { 40: 43, 32: [1, 46], 33: [1, 48], 34: [1, 44], 37: [1, 45], 41: [1, 47] }), { 27: 49, 33: g, 45: f }, { 32: [1, 50], 34: [1, 51] }, { 27: 52, 33: g, 45: f }, { 1: [2, 4] }, r(E, [2, 11]), r(i, [2, 16]), r(i, [2, 17]), r(i, [2, 21]), r(x, [2, 115]), r(x, [2, 116]), r(i, [2, 45]), { 33: [1, 53] }, { 38: 54, 42: p, 43: d, 44: y }, { 33: [1, 58] }, { 33: [1, 59] }, r(i, [2, 111]), r(i, [2, 29], { 32: [1, 60], 34: [1, 62], 37: [1, 61] }), { 33: [1, 63] }, { 33: [1, 64], 35: [1, 65] }, r(i, [2, 22], { 29: [1, 66] }), r(i, [2, 46], { 32: [1, 68], 37: [1, 67], 41: [1, 69] }), r(i, [2, 47], { 32: [1, 71], 34: [1, 70], 41: [1, 72] }), r(N, [2, 112]), r(N, [2, 113]), r(N, [2, 114]), r(i, [2, 50], { 34: [1, 73], 37: [1, 74], 41: [1, 75] }), r(i, [2, 61], { 32: [1, 78], 34: [1, 76], 37: [1, 77] }), { 33: [1, 79] }, { 38: 80, 42: p, 43: d, 44: y }, { 33: [1, 81] }, r(i, [2, 24], { 34: [1, 82] }), { 32: [1, 83] }, { 32: [1, 84] }, { 30: [1, 85] }, { 38: 86, 42: p, 43: d, 44: y }, { 33: [1, 87] }, { 33: [1, 88] }, { 33: [1, 89] }, { 33: [1, 90] }, { 33: [1, 91] }, { 33: [1, 92] }, { 38: 93, 42: p, 43: d, 44: y }, { 33: [1, 94] }, { 33: [1, 95] }, { 38: 96, 42: p, 43: d, 44: y }, { 33: [1, 97] }, r(i, [2, 30], { 34: [1, 99], 37: [1, 98] }), r(i, [2, 31], { 32: [1, 101], 34: [1, 100] }), r(i, [2, 32], { 32: [1, 102], 37: [1, 103] }), { 33: [1, 104], 35: [1, 105] }, { 33: [1, 106] }, { 33: [1, 107] }, r(i, [2, 23]), r(i, [2, 48], { 32: [1, 108], 41: [1, 109] }), r(i, [2, 52], { 37: [1, 110], 41: [1, 111] }), r(i, [2, 62], { 32: [1, 113], 37: [1, 112] }), r(i, [2, 49], { 32: [1, 114], 41: [1, 115] }), r(i, [2, 54], { 34: [1, 116], 41: [1, 117] }), r(i, [2, 65], { 32: [1, 119], 34: [1, 118] }), r(i, [2, 51], { 37: [1, 120], 41: [1, 121] }), r(i, [2, 53], { 34: [1, 122], 41: [1, 123] }), r(i, [2, 66], { 34: [1, 125], 37: [1, 124] }), r(i, [2, 63], { 32: [1, 127], 37: [1, 126] }), r(i, [2, 64], { 32: [1, 129], 34: [1, 128] }), r(i, [2, 67], { 34: [1, 131], 37: [1, 130] }), { 38: 132, 42: p, 43: d, 44: y }, { 33: [1, 133] }, { 33: [1, 134] }, { 33: [1, 135] }, { 33: [1, 136] }, { 38: 137, 42: p, 43: d, 44: y }, r(i, [2, 25]), r(i, [2, 26]), r(i, [2, 27]), r(i, [2, 28]), { 33: [1, 138] }, { 33: [1, 139] }, { 38: 140, 42: p, 43: d, 44: y }, { 33: [1, 141] }, { 38: 142, 42: p, 43: d, 44: y }, { 33: [1, 143] }, { 33: [1, 144] }, { 33: [1, 145] }, { 33: [1, 146] }, { 33: [1, 147] }, { 33: [1, 148] }, { 33: [1, 149] }, { 38: 150, 42: p, 43: d, 44: y }, { 33: [1, 151] }, { 33: [1, 152] }, { 33: [1, 153] }, { 38: 154, 42: p, 43: d, 44: y }, { 33: [1, 155] }, { 38: 156, 42: p, 43: d, 44: y }, { 33: [1, 157] }, { 33: [1, 158] }, { 33: [1, 159] }, { 38: 160, 42: p, 43: d, 44: y }, { 33: [1, 161] }, r(i, [2, 36], { 34: [1, 162] }), r(i, [2, 37], { 37: [1, 163] }), r(i, [2, 35], { 32: [1, 164] }), r(i, [2, 38], { 34: [1, 165] }), r(i, [2, 33], { 37: [1, 166] }), r(i, [2, 34], { 32: [1, 167] }), r(i, [2, 59], { 41: [1, 168] }), r(i, [2, 72], { 32: [1, 169] }), r(i, [2, 60], { 41: [1, 170] }), r(i, [2, 83], { 37: [1, 171] }), r(i, [2, 73], { 32: [1, 172] }), r(i, [2, 82], { 37: [1, 173] }), r(i, [2, 58], { 41: [1, 174] }), r(i, [2, 71], { 32: [1, 175] }), r(i, [2, 57], { 41: [1, 176] }), r(i, [2, 77], { 34: [1, 177] }), r(i, [2, 70], { 32: [1, 178] }), r(i, [2, 76], { 34: [1, 179] }), r(i, [2, 56], { 41: [1, 180] }), r(i, [2, 84], { 37: [1, 181] }), r(i, [2, 55], { 41: [1, 182] }), r(i, [2, 78], { 34: [1, 183] }), r(i, [2, 79], { 34: [1, 184] }), r(i, [2, 85], { 37: [1, 185] }), r(i, [2, 69], { 32: [1, 186] }), r(i, [2, 80], { 37: [1, 187] }), r(i, [2, 68], { 32: [1, 188] }), r(i, [2, 74], { 34: [1, 189] }), r(i, [2, 75], { 34: [1, 190] }), r(i, [2, 81], { 37: [1, 191] }), { 33: [1, 192] }, { 38: 193, 42: p, 43: d, 44: y }, { 33: [1, 194] }, { 33: [1, 195] }, { 38: 196, 42: p, 43: d, 44: y }, { 33: [1, 197] }, { 33: [1, 198] }, { 33: [1, 199] }, { 33: [1, 200] }, { 38: 201, 42: p, 43: d, 44: y }, { 33: [1, 202] }, { 38: 203, 42: p, 43: d, 44: y }, { 33: [1, 204] }, { 33: [1, 205] }, { 33: [1, 206] }, { 33: [1, 207] }, { 33: [1, 208] }, { 33: [1, 209] }, { 33: [1, 210] }, { 38: 211, 42: p, 43: d, 44: y }, { 33: [1, 212] }, { 33: [1, 213] }, { 33: [1, 214] }, { 38: 215, 42: p, 43: d, 44: y }, { 33: [1, 216] }, { 38: 217, 42: p, 43: d, 44: y }, { 33: [1, 218] }, { 33: [1, 219] }, { 33: [1, 220] }, { 38: 221, 42: p, 43: d, 44: y }, r(i, [2, 39]), r(i, [2, 41]), r(i, [2, 40]), r(i, [2, 42]), r(i, [2, 44]), r(i, [2, 43]), r(i, [2, 100]), r(i, [2, 101]), r(i, [2, 98]), r(i, [2, 99]), r(i, [2, 103]), r(i, [2, 102]), r(i, [2, 107]), r(i, [2, 106]), r(i, [2, 105]), r(i, [2, 104]), r(i, [2, 109]), r(i, [2, 108]), r(i, [2, 97]), r(i, [2, 96]), r(i, [2, 95]), r(i, [2, 94]), r(i, [2, 92]), r(i, [2, 93]), r(i, [2, 91]), r(i, [2, 90]), r(i, [2, 89]), r(i, [2, 88]), r(i, [2, 86]), r(i, [2, 87])],
    defaultActions: { 7: [2, 1], 13: [2, 2], 18: [2, 3], 36: [2, 4] },
    parseError: function(h, b) {
      if (b.recoverable)
        this.trace(h);
      else {
        var k = new Error(h);
        throw k.hash = b, k;
      }
    },
    parse: function(h) {
      var b = this, k = [0], s = [], T = [null], t = [], W = this.table, e = "", rt = 0, pt = 0, Lt = 2, bt = 1, Rt = t.slice.call(arguments, 1), M = Object.create(this.lexer), Y = { yy: {} };
      for (var ct in this.yy)
        Object.prototype.hasOwnProperty.call(this.yy, ct) && (Y.yy[ct] = this.yy[ct]);
      M.setInput(h, Y.yy), Y.yy.lexer = M, Y.yy.parser = this, typeof M.yylloc > "u" && (M.yylloc = {});
      var ot = M.yylloc;
      t.push(ot);
      var Mt = M.options && M.options.ranges;
      typeof Y.yy.parseError == "function" ? this.parseError = Y.yy.parseError : this.parseError = Object.getPrototypeOf(this).parseError;
      function Ct() {
        var j;
        return j = s.pop() || M.lex() || bt, typeof j != "number" && (j instanceof Array && (s = j, j = s.pop()), j = b.symbols_[j] || j), j;
      }
      for (var I, K, V, lt, J = {}, it, z, gt, st; ; ) {
        if (K = k[k.length - 1], this.defaultActions[K] ? V = this.defaultActions[K] : ((I === null || typeof I > "u") && (I = Ct()), V = W[K] && W[K][I]), typeof V > "u" || !V.length || !V[0]) {
          var ht = "";
          st = [];
          for (it in W[K])
            this.terminals_[it] && it > Lt && st.push("'" + this.terminals_[it] + "'");
          M.showPosition ? ht = "Parse error on line " + (rt + 1) + `:
` + M.showPosition() + `
Expecting ` + st.join(", ") + ", got '" + (this.terminals_[I] || I) + "'" : ht = "Parse error on line " + (rt + 1) + ": Unexpected " + (I == bt ? "end of input" : "'" + (this.terminals_[I] || I) + "'"), this.parseError(ht, {
            text: M.match,
            token: this.terminals_[I] || I,
            line: M.yylineno,
            loc: ot,
            expected: st
          });
        }
        if (V[0] instanceof Array && V.length > 1)
          throw new Error("Parse Error: multiple actions possible at state: " + K + ", token: " + I);
        switch (V[0]) {
          case 1:
            k.push(I), T.push(M.yytext), t.push(M.yylloc), k.push(V[1]), I = null, pt = M.yyleng, e = M.yytext, rt = M.yylineno, ot = M.yylloc;
            break;
          case 2:
            if (z = this.productions_[V[1]][1], J.$ = T[T.length - z], J._$ = {
              first_line: t[t.length - (z || 1)].first_line,
              last_line: t[t.length - 1].last_line,
              first_column: t[t.length - (z || 1)].first_column,
              last_column: t[t.length - 1].last_column
            }, Mt && (J._$.range = [
              t[t.length - (z || 1)].range[0],
              t[t.length - 1].range[1]
            ]), lt = this.performAction.apply(J, [
              e,
              pt,
              rt,
              Y.yy,
              V[1],
              T,
              t
            ].concat(Rt)), typeof lt < "u")
              return lt;
            z && (k = k.slice(0, -1 * z * 2), T = T.slice(0, -1 * z), t = t.slice(0, -1 * z)), k.push(this.productions_[V[1]][0]), T.push(J.$), t.push(J._$), gt = W[k[k.length - 2]][k[k.length - 1]], k.push(gt);
            break;
          case 3:
            return !0;
        }
      }
      return !0;
    }
  }, B = function() {
    var q = {
      EOF: 1,
      parseError: function(b, k) {
        if (this.yy.parser)
          this.yy.parser.parseError(b, k);
        else
          throw new Error(b);
      },
      // resets the lexer, sets new input
      setInput: function(h, b) {
        return this.yy = b || this.yy || {}, this._input = h, this._more = this._backtrack = this.done = !1, this.yylineno = this.yyleng = 0, this.yytext = this.matched = this.match = "", this.conditionStack = ["INITIAL"], this.yylloc = {
          first_line: 1,
          first_column: 0,
          last_line: 1,
          last_column: 0
        }, this.options.ranges && (this.yylloc.range = [0, 0]), this.offset = 0, this;
      },
      // consumes and returns one char from the input
      input: function() {
        var h = this._input[0];
        this.yytext += h, this.yyleng++, this.offset++, this.match += h, this.matched += h;
        var b = h.match(/(?:\r\n?|\n).*/g);
        return b ? (this.yylineno++, this.yylloc.last_line++) : this.yylloc.last_column++, this.options.ranges && this.yylloc.range[1]++, this._input = this._input.slice(1), h;
      },
      // unshifts one char (or a string) into the input
      unput: function(h) {
        var b = h.length, k = h.split(/(?:\r\n?|\n)/g);
        this._input = h + this._input, this.yytext = this.yytext.substr(0, this.yytext.length - b), this.offset -= b;
        var s = this.match.split(/(?:\r\n?|\n)/g);
        this.match = this.match.substr(0, this.match.length - 1), this.matched = this.matched.substr(0, this.matched.length - 1), k.length - 1 && (this.yylineno -= k.length - 1);
        var T = this.yylloc.range;
        return this.yylloc = {
          first_line: this.yylloc.first_line,
          last_line: this.yylineno + 1,
          first_column: this.yylloc.first_column,
          last_column: k ? (k.length === s.length ? this.yylloc.first_column : 0) + s[s.length - k.length].length - k[0].length : this.yylloc.first_column - b
        }, this.options.ranges && (this.yylloc.range = [T[0], T[0] + this.yyleng - b]), this.yyleng = this.yytext.length, this;
      },
      // When called from action, caches matched text and appends it on next action
      more: function() {
        return this._more = !0, this;
      },
      // When called from action, signals the lexer that this rule fails to match the input, so the next matching rule (regex) should be tested instead.
      reject: function() {
        if (this.options.backtrack_lexer)
          this._backtrack = !0;
        else
          return this.parseError("Lexical error on line " + (this.yylineno + 1) + `. You can only invoke reject() in the lexer when the lexer is of the backtracking persuasion (options.backtrack_lexer = true).
` + this.showPosition(), {
            text: "",
            token: null,
            line: this.yylineno
          });
        return this;
      },
      // retain first n characters of the match
      less: function(h) {
        this.unput(this.match.slice(h));
      },
      // displays already matched input, i.e. for error messages
      pastInput: function() {
        var h = this.matched.substr(0, this.matched.length - this.match.length);
        return (h.length > 20 ? "..." : "") + h.substr(-20).replace(/\n/g, "");
      },
      // displays upcoming input, i.e. for error messages
      upcomingInput: function() {
        var h = this.match;
        return h.length < 20 && (h += this._input.substr(0, 20 - h.length)), (h.substr(0, 20) + (h.length > 20 ? "..." : "")).replace(/\n/g, "");
      },
      // displays the character position where the lexing error occurred, i.e. for error messages
      showPosition: function() {
        var h = this.pastInput(), b = new Array(h.length + 1).join("-");
        return h + this.upcomingInput() + `
` + b + "^";
      },
      // test the lexed token: return FALSE when not a match, otherwise return token
      test_match: function(h, b) {
        var k, s, T;
        if (this.options.backtrack_lexer && (T = {
          yylineno: this.yylineno,
          yylloc: {
            first_line: this.yylloc.first_line,
            last_line: this.last_line,
            first_column: this.yylloc.first_column,
            last_column: this.yylloc.last_column
          },
          yytext: this.yytext,
          match: this.match,
          matches: this.matches,
          matched: this.matched,
          yyleng: this.yyleng,
          offset: this.offset,
          _more: this._more,
          _input: this._input,
          yy: this.yy,
          conditionStack: this.conditionStack.slice(0),
          done: this.done
        }, this.options.ranges && (T.yylloc.range = this.yylloc.range.slice(0))), s = h[0].match(/(?:\r\n?|\n).*/g), s && (this.yylineno += s.length), this.yylloc = {
          first_line: this.yylloc.last_line,
          last_line: this.yylineno + 1,
          first_column: this.yylloc.last_column,
          last_column: s ? s[s.length - 1].length - s[s.length - 1].match(/\r?\n?/)[0].length : this.yylloc.last_column + h[0].length
        }, this.yytext += h[0], this.match += h[0], this.matches = h, this.yyleng = this.yytext.length, this.options.ranges && (this.yylloc.range = [this.offset, this.offset += this.yyleng]), this._more = !1, this._backtrack = !1, this._input = this._input.slice(h[0].length), this.matched += h[0], k = this.performAction.call(this, this.yy, this, b, this.conditionStack[this.conditionStack.length - 1]), this.done && this._input && (this.done = !1), k)
          return k;
        if (this._backtrack) {
          for (var t in T)
            this[t] = T[t];
          return !1;
        }
        return !1;
      },
      // return next match in input
      next: function() {
        if (this.done)
          return this.EOF;
        this._input || (this.done = !0);
        var h, b, k, s;
        this._more || (this.yytext = "", this.match = "");
        for (var T = this._currentRules(), t = 0; t < T.length; t++)
          if (k = this._input.match(this.rules[T[t]]), k && (!b || k[0].length > b[0].length)) {
            if (b = k, s = t, this.options.backtrack_lexer) {
              if (h = this.test_match(k, T[t]), h !== !1)
                return h;
              if (this._backtrack) {
                b = !1;
                continue;
              } else
                return !1;
            } else if (!this.options.flex)
              break;
          }
        return b ? (h = this.test_match(b, T[s]), h !== !1 ? h : !1) : this._input === "" ? this.EOF : this.parseError("Lexical error on line " + (this.yylineno + 1) + `. Unrecognized text.
` + this.showPosition(), {
          text: "",
          token: null,
          line: this.yylineno
        });
      },
      // return next match that has a token
      lex: function() {
        var b = this.next();
        return b || this.lex();
      },
      // activates a new lexer condition state (pushes the new lexer condition state onto the condition stack)
      begin: function(b) {
        this.conditionStack.push(b);
      },
      // pop the previously active lexer condition state off the condition stack
      popState: function() {
        var b = this.conditionStack.length - 1;
        return b > 0 ? this.conditionStack.pop() : this.conditionStack[0];
      },
      // produce the lexer rule set which is active for the currently active lexer condition state
      _currentRules: function() {
        return this.conditionStack.length && this.conditionStack[this.conditionStack.length - 1] ? this.conditions[this.conditionStack[this.conditionStack.length - 1]].rules : this.conditions.INITIAL.rules;
      },
      // return the currently active lexer condition state; when an index argument is provided it produces the N-th previous condition state, if available
      topState: function(b) {
        return b = this.conditionStack.length - 1 - Math.abs(b || 0), b >= 0 ? this.conditionStack[b] : "INITIAL";
      },
      // alias for begin(condition)
      pushState: function(b) {
        this.begin(b);
      },
      // return the number of states currently on the stack
      stateStackSize: function() {
        return this.conditionStack.length;
      },
      options: { "case-insensitive": !0 },
      performAction: function(b, k, s, T) {
        switch (s) {
          case 0:
            return this.begin("acc_title"), 19;
          case 1:
            return this.popState(), "acc_title_value";
          case 2:
            return this.begin("acc_descr"), 21;
          case 3:
            return this.popState(), "acc_descr_value";
          case 4:
            this.begin("acc_descr_multiline");
            break;
          case 5:
            this.popState();
            break;
          case 6:
            return "acc_descr_multiline_value";
          case 7:
            return 13;
          case 8:
            break;
          case 9:
            break;
          case 10:
            return 5;
          case 11:
            return 39;
          case 12:
            return 32;
          case 13:
            return 37;
          case 14:
            return 41;
          case 15:
            return 42;
          case 16:
            return 43;
          case 17:
            return 44;
          case 18:
            return 34;
          case 19:
            return 28;
          case 20:
            return 29;
          case 21:
            return 36;
          case 22:
            return 31;
          case 23:
            return 26;
          case 24:
            return 9;
          case 25:
            return 9;
          case 26:
            return 8;
          case 27:
            return "CARET";
          case 28:
            this.begin("options");
            break;
          case 29:
            this.popState();
            break;
          case 30:
            return 12;
          case 31:
            return 35;
          case 32:
            this.begin("string");
            break;
          case 33:
            this.popState();
            break;
          case 34:
            return 33;
          case 35:
            return 30;
          case 36:
            return 45;
          case 37:
            return 7;
        }
      },
      rules: [/^(?:accTitle\s*:\s*)/i, /^(?:(?!\n||)*[^\n]*)/i, /^(?:accDescr\s*:\s*)/i, /^(?:(?!\n||)*[^\n]*)/i, /^(?:accDescr\s*\{\s*)/i, /^(?:[\}])/i, /^(?:[^\}]*)/i, /^(?:(\r?\n)+)/i, /^(?:#[^\n]*)/i, /^(?:%[^\n]*)/i, /^(?:gitGraph\b)/i, /^(?:commit(?=\s|$))/i, /^(?:id:)/i, /^(?:type:)/i, /^(?:msg:)/i, /^(?:NORMAL\b)/i, /^(?:REVERSE\b)/i, /^(?:HIGHLIGHT\b)/i, /^(?:tag:)/i, /^(?:branch(?=\s|$))/i, /^(?:order:)/i, /^(?:merge(?=\s|$))/i, /^(?:cherry-pick(?=\s|$))/i, /^(?:checkout(?=\s|$))/i, /^(?:LR\b)/i, /^(?:TB\b)/i, /^(?::)/i, /^(?:\^)/i, /^(?:options\r?\n)/i, /^(?:[ \r\n\t]+end\b)/i, /^(?:[\s\S]+(?=[ \r\n\t]+end))/i, /^(?:["]["])/i, /^(?:["])/i, /^(?:["])/i, /^(?:[^"]*)/i, /^(?:[0-9]+(?=\s|$))/i, /^(?:\w([-\./\w]*[-\w])?)/i, /^(?:$)/i, /^(?:\s+)/i],
      conditions: { acc_descr_multiline: { rules: [5, 6], inclusive: !1 }, acc_descr: { rules: [3], inclusive: !1 }, acc_title: { rules: [1], inclusive: !1 }, options: { rules: [29, 30], inclusive: !1 }, string: { rules: [33, 34], inclusive: !1 }, INITIAL: { rules: [0, 2, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 35, 36, 37, 38], inclusive: !0 } }
    };
    return q;
  }();
  w.lexer = B;
  function P() {
    this.yy = {};
  }
  return P.prototype = w, w.Parser = P, new P();
}();
mt.parser = mt;
const Dt = mt;
let at = O().gitGraph.mainBranchName, zt = O().gitGraph.mainBranchOrder, R = {}, S = null, Z = {};
Z[at] = { name: at, order: zt };
let L = {};
L[at] = S;
let v = at, xt = "LR", U = 0;
function ft() {
  return Ht({ length: 7 });
}
function jt(r, a) {
  const o = /* @__PURE__ */ Object.create(null);
  return r.reduce((u, n) => {
    const c = a(n);
    return o[c] || (o[c] = !0, u.push(n)), u;
  }, []);
}
const qt = function(r) {
  xt = r;
};
let yt = {};
const Yt = function(r) {
  G.debug("options str", r), r = r && r.trim(), r = r || "{}";
  try {
    yt = JSON.parse(r);
  } catch (a) {
    G.error("error while parsing gitGraph options", a.message);
  }
}, Kt = function() {
  return yt;
}, Ft = function(r, a, o, u) {
  G.debug("Entering commit:", r, a, o, u), a = D.sanitizeText(a, O()), r = D.sanitizeText(r, O()), u = D.sanitizeText(u, O());
  const n = {
    id: a || U + "-" + ft(),
    message: r,
    seq: U++,
    type: o || $.NORMAL,
    tag: u || "",
    parents: S == null ? [] : [S.id],
    branch: v
  };
  S = n, R[n.id] = n, L[v] = n.id, G.debug("in pushCommit " + n.id);
}, Ut = function(r, a) {
  if (r = D.sanitizeText(r, O()), L[r] === void 0)
    L[r] = S != null ? S.id : null, Z[r] = { name: r, order: a ? parseInt(a, 10) : null }, _t(r), G.debug("in createBranch");
  else {
    let o = new Error(
      'Trying to create an existing branch. (Help: Either use a new name if you want create a new branch or try using "checkout ' + r + '")'
    );
    throw o.hash = {
      text: "branch " + r,
      token: "branch " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ['"checkout ' + r + '"']
    }, o;
  }
}, Jt = function(r, a, o, u) {
  r = D.sanitizeText(r, O()), a = D.sanitizeText(a, O());
  const n = R[L[v]], c = R[L[r]];
  if (v === r) {
    let l = new Error('Incorrect usage of "merge". Cannot merge a branch to itself');
    throw l.hash = {
      text: "merge " + r,
      token: "merge " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ["branch abc"]
    }, l;
  } else if (n === void 0 || !n) {
    let l = new Error(
      'Incorrect usage of "merge". Current branch (' + v + ")has no commits"
    );
    throw l.hash = {
      text: "merge " + r,
      token: "merge " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ["commit"]
    }, l;
  } else if (L[r] === void 0) {
    let l = new Error(
      'Incorrect usage of "merge". Branch to be merged (' + r + ") does not exist"
    );
    throw l.hash = {
      text: "merge " + r,
      token: "merge " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ["branch " + r]
    }, l;
  } else if (c === void 0 || !c) {
    let l = new Error(
      'Incorrect usage of "merge". Branch to be merged (' + r + ") has no commits"
    );
    throw l.hash = {
      text: "merge " + r,
      token: "merge " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ['"commit"']
    }, l;
  } else if (n === c) {
    let l = new Error('Incorrect usage of "merge". Both branches have same head');
    throw l.hash = {
      text: "merge " + r,
      token: "merge " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ["branch abc"]
    }, l;
  } else if (a && R[a] !== void 0) {
    let l = new Error(
      'Incorrect usage of "merge". Commit with id:' + a + " already exists, use different custom Id"
    );
    throw l.hash = {
      text: "merge " + r + a + o + u,
      token: "merge " + r + a + o + u,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: [
        "merge " + r + " " + a + "_UNIQUE " + o + " " + u
      ]
    }, l;
  }
  const m = {
    id: a || U + "-" + ft(),
    message: "merged branch " + r + " into " + v,
    seq: U++,
    parents: [S == null ? null : S.id, L[r]],
    branch: v,
    type: $.MERGE,
    customType: o,
    customId: !!a,
    tag: u || ""
  };
  S = m, R[m.id] = m, L[v] = m.id, G.debug(L), G.debug("in mergeBranch");
}, Wt = function(r, a, o) {
  if (G.debug("Entering cherryPick:", r, a, o), r = D.sanitizeText(r, O()), a = D.sanitizeText(a, O()), o = D.sanitizeText(o, O()), !r || R[r] === void 0) {
    let c = new Error(
      'Incorrect usage of "cherryPick". Source commit id should exist and provided'
    );
    throw c.hash = {
      text: "cherryPick " + r + " " + a,
      token: "cherryPick " + r + " " + a,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ["cherry-pick abc"]
    }, c;
  }
  let u = R[r], n = u.branch;
  if (u.type === $.MERGE) {
    let c = new Error(
      'Incorrect usage of "cherryPick". Source commit should not be a merge commit'
    );
    throw c.hash = {
      text: "cherryPick " + r + " " + a,
      token: "cherryPick " + r + " " + a,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ["cherry-pick abc"]
    }, c;
  }
  if (!a || R[a] === void 0) {
    if (n === v) {
      let l = new Error(
        'Incorrect usage of "cherryPick". Source commit is already on current branch'
      );
      throw l.hash = {
        text: "cherryPick " + r + " " + a,
        token: "cherryPick " + r + " " + a,
        line: "1",
        loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
        expected: ["cherry-pick abc"]
      }, l;
    }
    const c = R[L[v]];
    if (c === void 0 || !c) {
      let l = new Error(
        'Incorrect usage of "cherry-pick". Current branch (' + v + ")has no commits"
      );
      throw l.hash = {
        text: "cherryPick " + r + " " + a,
        token: "cherryPick " + r + " " + a,
        line: "1",
        loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
        expected: ["cherry-pick abc"]
      }, l;
    }
    const m = {
      id: U + "-" + ft(),
      message: "cherry-picked " + u + " into " + v,
      seq: U++,
      parents: [S == null ? null : S.id, u.id],
      branch: v,
      type: $.CHERRY_PICK,
      tag: o ?? "cherry-pick:" + u.id
    };
    S = m, R[m.id] = m, L[v] = m.id, G.debug(L), G.debug("in cherryPick");
  }
}, _t = function(r) {
  if (r = D.sanitizeText(r, O()), L[r] === void 0) {
    let a = new Error(
      'Trying to checkout branch which is not yet created. (Help try using "branch ' + r + '")'
    );
    throw a.hash = {
      text: "checkout " + r,
      token: "checkout " + r,
      line: "1",
      loc: { first_line: 1, last_line: 1, first_column: 1, last_column: 1 },
      expected: ['"branch ' + r + '"']
    }, a;
  } else {
    v = r;
    const a = L[v];
    S = R[a];
  }
};
function dt(r, a, o) {
  const u = r.indexOf(a);
  u === -1 ? r.push(o) : r.splice(u, 1, o);
}
function Et(r) {
  const a = r.reduce((n, c) => n.seq > c.seq ? n : c, r[0]);
  let o = "";
  r.forEach(function(n) {
    n === a ? o += "	*" : o += "	|";
  });
  const u = [o, a.id, a.seq];
  for (let n in L)
    L[n] === a.id && u.push(n);
  if (G.debug(u.join(" ")), a.parents && a.parents.length == 2) {
    const n = R[a.parents[0]];
    dt(r, a, n), r.push(R[a.parents[1]]);
  } else {
    if (a.parents.length == 0)
      return;
    {
      const n = R[a.parents];
      dt(r, a, n);
    }
  }
  r = jt(r, (n) => n.id), Et(r);
}
const Xt = function() {
  G.debug(R);
  const r = wt()[0];
  Et([r]);
}, Qt = function() {
  R = {}, S = null;
  let r = O().gitGraph.mainBranchName, a = O().gitGraph.mainBranchOrder;
  L = {}, L[r] = null, Z = {}, Z[r] = { name: r, order: a }, v = r, U = 0, Pt();
}, Zt = function() {
  return Object.values(Z).map((a, o) => a.order !== null ? a : {
    ...a,
    order: parseFloat(`0.${o}`, 10)
  }).sort((a, o) => a.order - o.order).map(({ name: a }) => ({ name: a }));
}, $t = function() {
  return L;
}, te = function() {
  return R;
}, wt = function() {
  const r = Object.keys(R).map(function(a) {
    return R[a];
  });
  return r.forEach(function(a) {
    G.debug(a.id);
  }), r.sort((a, o) => a.seq - o.seq), r;
}, ee = function() {
  return v;
}, re = function() {
  return xt;
}, ie = function() {
  return S;
}, $ = {
  NORMAL: 0,
  REVERSE: 1,
  HIGHLIGHT: 2,
  MERGE: 3,
  CHERRY_PICK: 4
}, se = {
  getConfig: () => O().gitGraph,
  setDirection: qt,
  setOptions: Yt,
  getOptions: Kt,
  commit: Ft,
  branch: Ut,
  merge: Jt,
  cherryPick: Wt,
  checkout: _t,
  //reset,
  prettyPrint: Xt,
  clear: Qt,
  getBranchesAsObjArray: Zt,
  getBranches: $t,
  getCommits: te,
  getCommitsArray: wt,
  getCurrentBranch: ee,
  getDirection: re,
  getHead: ie,
  setAccTitle: vt,
  getAccTitle: At,
  getAccDescription: Ot,
  setAccDescription: St,
  setDiagramTitle: It,
  getDiagramTitle: Gt,
  commitType: $
};
let X = {};
const H = {
  NORMAL: 0,
  REVERSE: 1,
  HIGHLIGHT: 2,
  MERGE: 3,
  CHERRY_PICK: 4
}, F = 8;
let C = {}, tt = {}, nt = [], et = 0, A = "LR";
const ae = () => {
  C = {}, tt = {}, X = {}, et = 0, nt = [], A = "LR";
}, Tt = (r) => {
  const a = document.createElementNS("http://www.w3.org/2000/svg", "text");
  let o = [];
  typeof r == "string" ? o = r.split(/\\n|\n|<br\s*\/?>/gi) : Array.isArray(r) ? o = r : o = [];
  for (const u of o) {
    const n = document.createElementNS("http://www.w3.org/2000/svg", "tspan");
    n.setAttributeNS("http://www.w3.org/XML/1998/namespace", "xml:space", "preserve"), n.setAttribute("dy", "1em"), n.setAttribute("x", "0"), n.setAttribute("class", "row"), n.textContent = u.trim(), a.appendChild(n);
  }
  return a;
}, kt = (r, a, o) => {
  const u = ut().gitGraph, n = r.append("g").attr("class", "commit-bullets"), c = r.append("g").attr("class", "commit-labels");
  let m = 0;
  A === "TB" && (m = 30), Object.keys(a).sort((_, i) => a[_].seq - a[i].seq).forEach((_) => {
    const i = a[_], g = A === "TB" ? m + 10 : C[i.branch].pos, f = A === "TB" ? C[i.branch].pos : m + 10;
    if (o) {
      let x, p = i.customType !== void 0 && i.customType !== "" ? i.customType : i.type;
      switch (p) {
        case H.NORMAL:
          x = "commit-normal";
          break;
        case H.REVERSE:
          x = "commit-reverse";
          break;
        case H.HIGHLIGHT:
          x = "commit-highlight";
          break;
        case H.MERGE:
          x = "commit-merge";
          break;
        case H.CHERRY_PICK:
          x = "commit-cherry-pick";
          break;
        default:
          x = "commit-normal";
      }
      if (p === H.HIGHLIGHT) {
        const d = n.append("rect");
        d.attr("x", f - 10), d.attr("y", g - 10), d.attr("height", 20), d.attr("width", 20), d.attr(
          "class",
          `commit ${i.id} commit-highlight${C[i.branch].index % F} ${x}-outer`
        ), n.append("rect").attr("x", f - 6).attr("y", g - 6).attr("height", 12).attr("width", 12).attr(
          "class",
          `commit ${i.id} commit${C[i.branch].index % F} ${x}-inner`
        );
      } else if (p === H.CHERRY_PICK)
        n.append("circle").attr("cx", f).attr("cy", g).attr("r", 10).attr("class", `commit ${i.id} ${x}`), n.append("circle").attr("cx", f - 3).attr("cy", g + 2).attr("r", 2.75).attr("fill", "#fff").attr("class", `commit ${i.id} ${x}`), n.append("circle").attr("cx", f + 3).attr("cy", g + 2).attr("r", 2.75).attr("fill", "#fff").attr("class", `commit ${i.id} ${x}`), n.append("line").attr("x1", f + 3).attr("y1", g + 1).attr("x2", f).attr("y2", g - 5).attr("stroke", "#fff").attr("class", `commit ${i.id} ${x}`), n.append("line").attr("x1", f - 3).attr("y1", g + 1).attr("x2", f).attr("y2", g - 5).attr("stroke", "#fff").attr("class", `commit ${i.id} ${x}`);
      else {
        const d = n.append("circle");
        if (d.attr("cx", f), d.attr("cy", g), d.attr("r", i.type === H.MERGE ? 9 : 10), d.attr(
          "class",
          `commit ${i.id} commit${C[i.branch].index % F}`
        ), p === H.MERGE) {
          const y = n.append("circle");
          y.attr("cx", f), y.attr("cy", g), y.attr("r", 6), y.attr(
            "class",
            `commit ${x} ${i.id} commit${C[i.branch].index % F}`
          );
        }
        p === H.REVERSE && n.append("path").attr("d", `M ${f - 5},${g - 5}L${f + 5},${g + 5}M${f - 5},${g + 5}L${f + 5},${g - 5}`).attr(
          "class",
          `commit ${x} ${i.id} commit${C[i.branch].index % F}`
        );
      }
    }
    if (A === "TB" ? tt[i.id] = { x: f, y: m + 10 } : tt[i.id] = { x: m + 10, y: g }, o) {
      if (i.type !== H.CHERRY_PICK && (i.customId && i.type === H.MERGE || i.type !== H.MERGE) && u.showCommitLabel) {
        const d = c.append("g"), y = d.insert("rect").attr("class", "commit-label-bkg"), N = d.append("text").attr("x", m).attr("y", g + 25).attr("class", "commit-label").text(i.id);
        let w = N.node().getBBox();
        if (y.attr("x", m + 10 - w.width / 2 - 2).attr("y", g + 13.5).attr("width", w.width + 2 * 2).attr("height", w.height + 2 * 2), A === "TB" && (y.attr("x", f - (w.width + 4 * 4 + 5)).attr("y", g - 12), N.attr("x", f - (w.width + 4 * 4)).attr("y", g + w.height - 12)), A !== "TB" && N.attr("x", m + 10 - w.width / 2), u.rotateCommitLabel)
          if (A === "TB")
            N.attr("transform", "rotate(-45, " + f + ", " + g + ")"), y.attr("transform", "rotate(-45, " + f + ", " + g + ")");
          else {
            let B = -7.5 - (w.width + 10) / 25 * 9.5, P = 10 + w.width / 25 * 8.5;
            d.attr(
              "transform",
              "translate(" + B + ", " + P + ") rotate(-45, " + m + ", " + g + ")"
            );
          }
      }
      if (i.tag) {
        const d = c.insert("polygon"), y = c.append("circle"), N = c.append("text").attr("y", g - 16).attr("class", "tag-label").text(i.tag);
        let w = N.node().getBBox();
        N.attr("x", m + 10 - w.width / 2);
        const B = w.height / 2, P = g - 19.2;
        d.attr("class", "tag-label-bkg").attr(
          "points",
          `
          ${m - w.width / 2 - 4 / 2},${P + 2}
          ${m - w.width / 2 - 4 / 2},${P - 2}
          ${m + 10 - w.width / 2 - 4},${P - B - 2}
          ${m + 10 + w.width / 2 + 4},${P - B - 2}
          ${m + 10 + w.width / 2 + 4},${P + B + 2}
          ${m + 10 - w.width / 2 - 4},${P + B + 2}`
        ), y.attr("cx", m - w.width / 2 + 4 / 2).attr("cy", P).attr("r", 1.5).attr("class", "tag-hole"), A === "TB" && (d.attr("class", "tag-label-bkg").attr(
          "points",
          `
            ${f},${m + 2}
            ${f},${m - 2}
            ${f + 10},${m - B - 2}
            ${f + 10 + w.width + 4},${m - B - 2}
            ${f + 10 + w.width + 4},${m + B + 2}
            ${f + 10},${m + B + 2}`
        ).attr("transform", "translate(12,12) rotate(45, " + f + "," + m + ")"), y.attr("cx", f + 4 / 2).attr("cy", m).attr("transform", "translate(12,12) rotate(45, " + f + "," + m + ")"), N.attr("x", f + 5).attr("y", m + 3).attr("transform", "translate(14,14) rotate(45, " + f + "," + m + ")"));
      }
    }
    m += 50, m > et && (et = m);
  });
}, ne = (r, a, o) => Object.keys(o).filter((c) => o[c].branch === a.branch && o[c].seq > r.seq && o[c].seq < a.seq).length > 0, Q = (r, a, o = 0) => {
  const u = r + Math.abs(r - a) / 2;
  if (o > 5)
    return u;
  if (nt.every((m) => Math.abs(m - u) >= 10))
    return nt.push(u), u;
  const c = Math.abs(r - a);
  return Q(r, a - c / 5, o + 1);
}, ce = (r, a, o, u) => {
  const n = tt[a.id], c = tt[o.id], m = ne(a, o, u);
  let l = "", E = "", _ = 0, i = 0, g = C[o.branch].index, f;
  if (m) {
    l = "A 10 10, 0, 0, 0,", E = "A 10 10, 0, 0, 1,", _ = 10, i = 10, g = C[o.branch].index;
    const x = n.y < c.y ? Q(n.y, c.y) : Q(c.y, n.y), p = n.x < c.x ? Q(n.x, c.x) : Q(c.x, n.x);
    A === "TB" ? n.x < c.x ? f = `M ${n.x} ${n.y} L ${p - _} ${n.y} ${E} ${p} ${n.y + i} L ${p} ${c.y - _} ${l} ${p + i} ${c.y} L ${c.x} ${c.y}` : f = `M ${n.x} ${n.y} L ${p + _} ${n.y} ${l} ${p} ${n.y + i} L ${p} ${c.y - _} ${E} ${p - i} ${c.y} L ${c.x} ${c.y}` : n.y < c.y ? f = `M ${n.x} ${n.y} L ${n.x} ${x - _} ${l} ${n.x + i} ${x} L ${c.x - _} ${x} ${E} ${c.x} ${x + i} L ${c.x} ${c.y}` : f = `M ${n.x} ${n.y} L ${n.x} ${x + _} ${E} ${n.x + i} ${x} L ${c.x - _} ${x} ${l} ${c.x} ${x - i} L ${c.x} ${c.y}`;
  } else
    A === "TB" ? (n.x < c.x && (l = "A 20 20, 0, 0, 0,", E = "A 20 20, 0, 0, 1,", _ = 20, i = 20, g = C[o.branch].index, f = `M ${n.x} ${n.y} L ${c.x - _} ${n.y} ${E} ${c.x} ${n.y + i} L ${c.x} ${c.y}`), n.x > c.x && (l = "A 20 20, 0, 0, 0,", E = "A 20 20, 0, 0, 1,", _ = 20, i = 20, g = C[a.branch].index, f = `M ${n.x} ${n.y} L ${n.x} ${c.y - _} ${E} ${n.x - i} ${c.y} L ${c.x} ${c.y}`), n.x === c.x && (g = C[a.branch].index, f = `M ${n.x} ${n.y} L ${n.x + _} ${n.y} ${l} ${n.x + i} ${c.y + _} L ${c.x} ${c.y}`)) : (n.y < c.y && (l = "A 20 20, 0, 0, 0,", _ = 20, i = 20, g = C[o.branch].index, f = `M ${n.x} ${n.y} L ${n.x} ${c.y - _} ${l} ${n.x + i} ${c.y} L ${c.x} ${c.y}`), n.y > c.y && (l = "A 20 20, 0, 0, 0,", _ = 20, i = 20, g = C[a.branch].index, f = `M ${n.x} ${n.y} L ${c.x - _} ${n.y} ${l} ${c.x} ${n.y - i} L ${c.x} ${c.y}`), n.y === c.y && (g = C[a.branch].index, f = `M ${n.x} ${n.y} L ${n.x} ${c.y - _} ${l} ${n.x + i} ${c.y} L ${c.x} ${c.y}`));
  r.append("path").attr("d", f).attr("class", "arrow arrow" + g % F);
}, oe = (r, a) => {
  const o = r.append("g").attr("class", "commit-arrows");
  Object.keys(a).forEach((u) => {
    const n = a[u];
    n.parents && n.parents.length > 0 && n.parents.forEach((c) => {
      ce(o, a[c], n, a);
    });
  });
}, le = (r, a) => {
  const o = ut().gitGraph, u = r.append("g");
  a.forEach((n, c) => {
    const m = c % F, l = C[n.name].pos, E = u.append("line");
    E.attr("x1", 0), E.attr("y1", l), E.attr("x2", et), E.attr("y2", l), E.attr("class", "branch branch" + m), A === "TB" && (E.attr("y1", 30), E.attr("x1", l), E.attr("y2", et), E.attr("x2", l)), nt.push(l);
    let _ = n.name;
    const i = Tt(_), g = u.insert("rect"), x = u.insert("g").attr("class", "branchLabel").insert("g").attr("class", "label branch-label" + m);
    x.node().appendChild(i);
    let p = i.getBBox();
    g.attr("class", "branchLabelBkg label" + m).attr("rx", 4).attr("ry", 4).attr("x", -p.width - 4 - (o.rotateCommitLabel === !0 ? 30 : 0)).attr("y", -p.height / 2 + 8).attr("width", p.width + 18).attr("height", p.height + 4), x.attr(
      "transform",
      "translate(" + (-p.width - 14 - (o.rotateCommitLabel === !0 ? 30 : 0)) + ", " + (l - p.height / 2 - 1) + ")"
    ), A === "TB" && (g.attr("x", l - p.width / 2 - 10).attr("y", 0), x.attr("transform", "translate(" + (l - p.width / 2 - 5) + ", 0)")), A !== "TB" && g.attr("transform", "translate(-19, " + (l - p.height / 2) + ")");
  });
}, he = function(r, a, o, u) {
  ae();
  const n = ut(), c = n.gitGraph;
  G.debug("in gitgraph renderer", r + `
`, "id:", a, o), X = u.db.getCommits();
  const m = u.db.getBranchesAsObjArray();
  A = u.db.getDirection();
  const l = Nt(`[id="${a}"]`);
  let E = 0;
  m.forEach((_, i) => {
    const g = Tt(_.name), f = l.append("g"), x = f.insert("g").attr("class", "branchLabel"), p = x.insert("g").attr("class", "label branch-label");
    p.node().appendChild(g);
    let d = g.getBBox();
    C[_.name] = { pos: E, index: i }, E += 50 + (c.rotateCommitLabel ? 40 : 0) + (A === "TB" ? d.width / 2 : 0), p.remove(), x.remove(), f.remove();
  }), kt(l, X, !1), c.showBranches && le(l, m), oe(l, X), kt(l, X, !0), Bt.insertTitle(
    l,
    "gitTitleText",
    c.titleTopMargin,
    u.db.getDiagramTitle()
  ), Vt(
    void 0,
    l,
    c.diagramPadding,
    c.useMaxWidth ?? n.useMaxWidth
  );
}, me = {
  draw: he
}, ue = (r) => `
  .commit-id,
  .commit-msg,
  .branch-label {
    fill: lightgrey;
    color: lightgrey;
    font-family: 'trebuchet ms', verdana, arial, sans-serif;
    font-family: var(--mermaid-font-family);
  }
  ${[0, 1, 2, 3, 4, 5, 6, 7].map(
  (a) => `
        .branch-label${a} { fill: ${r["gitBranchLabel" + a]}; }
        .commit${a} { stroke: ${r["git" + a]}; fill: ${r["git" + a]}; }
        .commit-highlight${a} { stroke: ${r["gitInv" + a]}; fill: ${r["gitInv" + a]}; }
        .label${a}  { fill: ${r["git" + a]}; }
        .arrow${a} { stroke: ${r["git" + a]}; }
        `
).join(`
`)}

  .branch {
    stroke-width: 1;
    stroke: ${r.lineColor};
    stroke-dasharray: 2;
  }
  .commit-label { font-size: ${r.commitLabelFontSize}; fill: ${r.commitLabelColor};}
  .commit-label-bkg { font-size: ${r.commitLabelFontSize}; fill: ${r.commitLabelBackground}; opacity: 0.5; }
  .tag-label { font-size: ${r.tagLabelFontSize}; fill: ${r.tagLabelColor};}
  .tag-label-bkg { fill: ${r.tagLabelBackground}; stroke: ${r.tagLabelBorder}; }
  .tag-hole { fill: ${r.textColor}; }

  .commit-merge {
    stroke: ${r.primaryColor};
    fill: ${r.primaryColor};
  }
  .commit-reverse {
    stroke: ${r.primaryColor};
    fill: ${r.primaryColor};
    stroke-width: 3;
  }
  .commit-highlight-outer {
  }
  .commit-highlight-inner {
    stroke: ${r.primaryColor};
    fill: ${r.primaryColor};
  }

  .arrow { stroke-width: 8; stroke-linecap: round; fill: none}
  .gitTitleText {
    text-anchor: middle;
    font-size: 18px;
    fill: ${r.textColor};
  }
`, fe = ue, be = {
  parser: Dt,
  db: se,
  renderer: me,
  styles: fe
};
export {
  be as diagram
};
