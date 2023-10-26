# -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2022 NEW ENTITY OPERATIONS INC. ALL RIGHTS RESERVED
CREATED: 2022/02/13
INSTANCE: KEYS->pool-> block
MODIFIED: 2022/11/05
OVERVIEW: Utilize various block allocation types to generate keys
HISTORY: VERSION 0.0.3
-> 2020/08/24 (VERSION 0.0.2)
-> 2022/02/13 (VERSION 0.0.1)
"""
__version__ = "0.0.3"
__author__ = "Ryan McKenna"
__copyright__ = "Copyright (C) 2023 CORE.HOST, LLC."
__credits__ = [
 "Ryan McKenna",
 "New Entity Operations Inc.", "New Entity Operations, LLC"]
__email__ = "Operator@NewEntityOperations.com"
__license__ = "New Entity License"
__maintainer__ = "Ryan McKenna"
__status__ = "Production"

## Assignment-generator bank: POOL_*

## Digit-only logic
POOL_DIGITAL_LOGIC = [
 0, 1
]
## Digit-Boolean logic
POOL_DIGITAL_BOOL = [
 True, False
]
## Digit-Real-number logic
POOL_DIGITAL_NUMBERS = [
 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]
## String-number logic
POOL_REAL_NUMBERS = [
 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]
## String-number logic
POOL_MATRIX_MULTIPLIER_COOMMON = [
 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000
]
POOL_MATRIX_MULTIPLIER_COMPLEX = [
 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000,
 100000000000000, 1000000000000000, 10000000000000000, 100000000000000000,
 1000000000000000000
]
## Pixel logic
POOL_PIXEL = [
 1
]
GRID_LENGTH = 10
DENSITY_MULTIPLIER = 1000
POOL_PIXEL_DENSITY = (POOL_PIXEL[0]*DENSITY_MULTIPLIER)/GRID_LENGTH
POOL_PIXEL_DENSITY = [
 POOL_PIXEL_DENSITY # PPI
]
POOL_PIXEL_VALUE_DICTIONARY = {
 0: ["on", "black"],
 1: ["off", "white"]
}
## Rainbow logic
POOL_COLOR_INPUT_DICTIONARY = {
 "r": ["rods", "resolution"],
 "c": ["cones", "color"]
}
POOL_COLOR_INPUT_DICTIONARY = {
 "r": ["rods", "resolution"],
 "c": ["cones", "color"]
}
POOL_COLOR_WAVE_DICTIONARY = {
 "L": ["Long-wavelength", "red", 710],
 "M": ["Medium-wavelength," "green", 675],
 "S": ["Short-wavelength", "blue", 550]
}
# R for Red, G for Green, B for Blue
POOL_COLOR_ADDITIVE_DICTIONARY_STANDARD = {
 "ALL": "white",
 "RG": "yellow",
 "RB": "purple",
 "BG": "green"
}
# decimal: [3-bit, has-color, not-color, color]
POOL_COLOR_VALUE_DECIMAL_DICTIONARY = {
 0: ["000", None, "R,G,B", "black"],
 1: ["001", "B", "R,G", "blue"],
 2: ["010", "G", "R,B", "green"],
 3: ["011", "G,B", "R", "cyan"],
 4: ["100", "R", "G,B", "red"],
 5: ["101", "R,B", "G", "magenta"],
 6: ["110", "R,G", "B", "yellow"],
 7: ["111", "R,G,B", None, "white"]
}
POOL_COLOR_VALUE_DECIMAL_24_BIT = {
 # 24 bit values: R8, G8, B8
 # 0xff = 255, & = bitwise, >> = shift n bits to the right or divide by 2^n
 0: ["R", "(pixel >> 16) & 0xff"],
 1: ["G", "(pixel >> 8) & 0xff"],
 2: ["B", "pixel & 0xff"]
}
POOL_COLOR_VALUE_DECIMAL_32_BIT_ALPHA = {
 # 32 bit values: R8, G8, B8, A8 (transparency)
 # 0xff = 255, & = bitwise, >> = shift n bits to the right or divide by 2^n
 0: ["R", "(pixel >> 16) & 0xff"],
 1: ["G", "(pixel >> 8) & 0xff"],
 2: ["B", "pixel & 0xff"],
 4: ["A", "pixel & 0xff"]
}
## String: Letter-based representation
POOL_LOWERCASE_LETTERS = [
 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]
POOL_UPPERCASE_CHARACTER = [
 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]
## String: Valid key representation
POOL_EXTENDED_CHARACTER = [
 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
 "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~", "`", "-",
 "_", "{", "}", "[", "]", "\\", "|", ":", ";", "'", '"', ",",
 "<", ">", ".", ",", "?", "/"
]
## Generate a pool from a random hash
POOL_RANDOM_BLOCK = [
 "A2134ADTFNLSP*(#AHH;LDPMNVLSPHIEFOPAHIAPEIHFPIA*(*#$WAHEHA92H:SHAHD)(*#$"
]
## Create a bucket for holding random numbers, assigned to unencrypted drives
## in the 12 bit sequence - Use the imported character pool of your choice
POOL_STANDARD_CHARACTER = [
 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]
## Dictionary-system standard encodings by decimal
## Categories can be looked up by decimal value: No aggregate table
## is assembled
POOL_DICTIONARY_DECIMAL_TO_BINARY = {
 0: "0", 1: "1", 2: "10", 3: "11", 4: "100", 5: "101", 6: "110", 7: "111",
 8: "1000", 9: "1001", 10: "1010",
 11: "1011", 12: "1100", 13: "1101", 14: "1110", 15: "1111", 16: "10000",
 17: "10001", 18: "10010",
 19: "10011", 20: "10100", 21: "10101", 22: "10110", 23: "10111",
 24: "11000", 25: "11001", 26: "11010",
 27: "11011", 28: "11100", 29: "11101", 30: "11110", 31: "11111",
 32: "100000", 33: "100001", 34: "100010",
 35: "100011", 36: "100100", 37: "100101", 38: "100110", 39: "100111",
 40: "101000", 41: "101001",
 42: "101010", 43: "101011", 44: "101100", 45: "101101", 46: "101110",
 47: "101111", 48: "110000",
 49: "110001", 50: "110010", 51: "110011", 52: "110100", 53: "110101",
 54: "110110", 55: "110111",
 56: "111000", 57: "111001", 58: "111010", 59: "111011", 60: "111100",
 61: "111101", 62: "111110",
 63: "111111", 64: "1000000", 65: "1000001", 66: "1000010", 67: "1000011",
 68: "1000100", 69: "1000101",
 70: "1000110", 71: "1000111", 72: "1001000", 73: "1001001", 74: "1001010",
 75: "1001011", 76: "1001100",
 77: "1001101", 78: "1001110", 79: "1001111", 80: "1010000", 81: "1010001",
 82: "1010010", 83: "1010011",
 84: "1010100", 85: "1010101", 86: "1010110", 87: "1010111", 88: "1011000",
 89: "1011001", 90: "1011010",
 91: "1011011", 92: "1011100", 93: "1011101", 94: "1011110", 95: "1011111",
 96: "1100000", 97: "1100001",
 98: "1100010", 99: "1100011", 100: "1100100", 101: "1100101", 102: "1100110",
 103: "1100111", 104: "1101000",
 105: "1101001", 106: "1101010", 107: "1101011", 108: "1101100",
 109: "1101101", 110: "1101110", 111: "1101111",
 112: "1110000", 113: "1110001", 114: "1110010", 115: "1110011",
 116: "1110100", 117: "1110101", 118: "1110110",
 119: "1110111", 120: "1111000", 121: "1111001", 122: "1111010",
 123: "1111011", 124: "1111100", 125: "1111101",
 126: "1111110", 127: "1111111", 128: "10000000", 129: "10000001",
 130: "10000010", 131: "10000011",
 132: "10000100", 133: "10000101", 134: "10000110", 135: "10000111",
 136: "10001000", 137: "10001001",
 138: "10001010", 139: "10001011", 140: "10001100", 141: "10001101",
 142: "10001110", 143: "10001111",
 144: "10010000", 145: "10010001", 146: "10010010", 147: "10010011",
 148: "10010100", 149: "10010101",
 150: "10010110", 151: "10010111", 152: "10011000", 153: "10011001",
 154: "10011010", 155: "10011011",
 156: "10011100", 157: "10011101", 158: "10011110", 159: "10011111",
 160: "10100000", 161: "10100001",
 162: "10100010", 163: "10100011", 164: "10100100", 165: "10100101",
 166: "10100110", 167: "10100111",
 168: "10101000", 169: "10101001", 170: "10101010", 171: "10101011",
 172: "10101100", 173: "10101101",
 174: "10101110", 175: "10101111", 176: "10110000", 177: "10110001",
 178: "10110010", 179: "10110011",
 180: "10110100", 181: "10110101", 182: "10110110", 183: "10110111",
 184: "10111000", 185: "10111001",
 186: "10111010", 187: "10111011", 188: "10111100", 189: "10111101",
 190: "10111110", 191: "10111111",
 192: "11000000", 193: "11000001", 194: "11000010", 195: "11000011",
 196: "11000100", 197: "11000101",
 198: "11000110", 199: "11000111", 200: "11001000", 201: "11001001",
 202: "11001010", 203: "11001011",
 204: "11001100", 205: "11001101", 206: "11001110", 207: "11001111",
 208: "11010000", 209: "11010001",
 210: "11010010", 211: "11010011", 212: "11010100", 213: "11010101",
 214: "11010110", 215: "11010111",
 216: "11011000", 217: "11011001", 218: "11011010", 219: "11011011",
 220: "11011100", 221: "11011101",
 222: "11011110", 223: "11011111", 224: "11100000", 225: "11100001",
 226: "11100010", 227: "11100011",
 228: "11100100", 229: "11100101", 230: "11100110", 231: "11100111",
 232: "11101000", 233: "11101001",
 234: "11101010", 235: "11101011", 236: "11101100", 237: "11101101",
 238: "11101110", 239: "11101111",
 240: "11110000", 241: "11110001", 242: "11110010", 243: "11110011",
 244: "11110100", 245: "11110101",
 246: "11110110", 247: "11110111", 248: "11111000", 249: "11111001",
 250: "11111010", 251: "11111011",
 252: "11111100", 253: "11111101", 254: "11111110", 255: "11111111 "
}
## Operations Methods: Classic
POOL_DICIONTARY_DECIMAL_TO_CHARACTER = {
 0: "NUL", 1: "SOH", 2: "STX", 3: "ETX", 4: "EOT", 5: "ENQ", 6: "ACK",
 7: "BEL", 8: "BS", 9: "HT", 10: "LF",
 11: "VT", 12: "FF", 13: "CR", 14: "SO", 15: "SI", 16: "DLE", 17: "DC1",
 18: "DC2", 19: "DC3", 20: "DC4",
 21: "NAK", 22: "SYN", 23: "ETB", 24: "CAN", 25: "EM", 26: "SUB", 27: "ESC",
 28: "FS", 29: "GS", 30: "RS",
 31: "US", 32: "SP", 33: "!", 34: '"', 35: "\#", 36: "$", 37: "%", 38: "&",
 39: "'", 40: "(",
 41: ")", 42: "*", 43: "+", 44: ",", 45: "-", 46: ".", 47: "/", 48: "0",
 49: "1", 50: "2",
 51: "3", 52: "4", 53: "5", 54: "6", 55: "7", 56: "8", 57: "9", 58: ":",
 59: ";", 60: "<",
 61: "=", 62: ">", 63: "?", 64: "@", 65: "A", 66: "B", 67: "C", 68: "D",
 69: "E", 70: "F",
 71: "G", 72: "H", 73: "I", 74: "J", 75: "K", 76: "L", 77: "M", 78: "N",
 79: "O", 80: "P",
 81: "Q", 82: "R", 83: "S", 84: "T", 85: "U", 86: "V", 87: "W", 88: "X",
 89: "Y", 90: "Z",
 91: "[", 92: "\\", 93: "]", 94: "^", 95: "_", 96: "`", 97: "a", 98: "b",
 99: "c", 100: "d",
 101: "e", 102: "f", 103: "g", 104: "h", 105: "i", 106: "j", 107: "k",
 108: "l", 109: "m", 110: "n",
 111: "o", 112: "p", 113: "q", 114: "r", 115: "s", 116: "t", 117: "u",
 118: "v", 119: "w", 120: "x",
 121: "y", 122: "z", 123: "{", 124: "|", 125: "}", 126: "~", 127: "DEL",
 128: "€", 129: "None", 130: "‚",
 131: "ƒ", 132: "„", 133: "…", 134: "†", 135: "‡", 136: "ˆ", 137: "‰",
 138: "Š", 139: "‹", 140: "Œ",
 141: "None", 142: "Ž", 143: "None", 144: "None", 145: "‘", 146: "’",
 147: '"', 148: "”", 149: "•", 150: "–",
 151: "—", 152: "˜", 153: "™", 154: "š", 155: "›", 156: "œ", 157: "None",
 158: "ž", 159: "Ÿ", 160: "NBSP",
 161: "¡", 162: "¢", 163: "£", 164: "¤", 165: "¥", 166: "¦", 167: "§",
 168: "¨", 169: "©", 170: "ª",
 171: "«", 172: "¬", 173: "None", 174: "®", 175: "¯", 176: "°", 177: "±",
 178: "²", 179: "³", 180: "´",
 181: "µ", 182: "¶", 183: "·", 184: "¸", 185: "¹", 186: "º", 187: "»",
 188: "¼", 189: "½", 190: "¾",
 191: "¿", 192: "À", 193: "Á", 194: "Â", 195: "Ã", 196: "Ä", 197: "Å",
 198: "Æ", 199: "Ç", 200: "È",
 201: "É", 202: "Ê", 203: "Ë", 204: "Ì", 205: "Í", 206: "Î", 207: "Ï",
 208: "Ð", 209: "Ñ", 210: "Ò",
 211: "Ó", 212: "Ô", 213: "Õ", 214: "Ö", 215: "×", 216: "Ø", 217: "Ù",
 218: "Ú", 219: "Û", 220: "Ü",
 221: "Ý", 222: "Þ", 223: "ß", 224: "à", 225: "á", 226: "â", 227: "ã",
 228: "ä", 229: "å", 230: "æ",
 231: "ç", 232: "è", 233: "é", 234: "ê", 235: "ë", 236: "ì", 237: "í",
 238: "î", 239: "ï", 240: "ð",
 241: "ñ", 242: "ò", 243: "ó", 244: "ô", 245: "õ", 246: "ö", 247: "÷",
 248: "ø", 249: "ù", 250: "ú",
 251: "û", 252: "ü", 253: "ý", 254: "þ", 255: "ÿ "
}
## Operations Methods: Verbose
POOL_DICTIONARY_TO_DESCRIPTION = {
 0: "Null", 1: "Start of Header", 2: "Start of Text", 3: "End of Text",
 4: "End of Transmission", 5: "Enquiry",
 6: "Acknowledge", 7: "Bell", 8: "Backspace", 9: "Horizontal Tab",
 10: "Newline / Line Feed", 11: "Vertical Tab",
 12: "Form Feed", 13: "Carriage Return", 14: "Shift Out", 15: "Shift In",
 16: "Data Link Escape",
 17: "Device Control 1", 18: "Device Control 2", 19: "Device Control 3",
 20: "Device Control 4",
 21: "Negative Acknowledge", 22: "Synchronize",
 23: "End of Transmission Block", 24: "Cancel",
 25: "End of Medium", 26: "Substitute", 27: "Escape", 28: "File Separator",
 29: "Group Separator",
 30: "Record Separator", 31: "Unit Separator", 32: "Space",
 33: "Exclamation mark", 34: "Double quote",
 35: "Number", 36: "Dollar", 37: "Percent", 38: "Ampersand",
 39: "Single quote", 40: "Left parenthesis",
 41: "Right parenthesis", 42: "Asterisk", 43: "Plus", 44: "Comma",
 45: "Minus", 46: "Period", 47: "Slash",
 48: "Zero", 49: "One", 50: "Two", 51: "Three", 52: "Four", 53: "Five",
 54: "Six", 55: "Seven", 56: "Eight",
 57: "Nine", 58: "Colon", 59: "Semicolon", 60: "Less than", 61: "Equal sign",
 62: "Greater than",
 63: "Question mark", 64: "At sign", 65: "Uppercase A", 66: "Uppercase B",
 67: "Uppercase C",
 68: "Uppercase D", 69: "Uppercase E", 70: "Uppercase F", 71: "Uppercase G",
 72: "Uppercase H",
 73: "Uppercase I", 74: "Uppercase J", 75: "Uppercase K", 76: "Uppercase L",
 77: "Uppercase M",
 78: "Uppercase N", 79: "Uppercase O", 80: "Uppercase P", 81: "Uppercase Q",
 82: "Uppercase R",
 83: "Uppercase S", 84: "Uppercase T", 85: "Uppercase U", 86: "Uppercase V",
 87: "Uppercase W",
 88: "Uppercase X", 89: "Uppercase Y", 90: "Uppercase Z",
 91: "Left square bracket", 92: "backslash",
 93: "Right square bracket", 94: "Caret / circumflex", 95: "Underscore",
 96: "Grave / accent", 97: "Lowercase a",
 98: "Lowercase b", 99: "Lowercase c", 100: "Lowercase d",
 101: "Lowercase e", 102: "Lowercase",
 103: "Lowercase g", 104: "Lowercase h", 105: "Lowercase i",
 106: "Lowercase j", 107: "Lowercase k",
 108: "Lowercase l", 109: "Lowercase m", 110: "Lowercase n",
 111: "Lowercase o", 112: "Lowercase p",
 113: "Lowercase q", 114: "Lowercase r", 115: "Lowercase s",
 116: "Lowercase t", 117: "Lowercase u",
 118: "Lowercase v", 119: "Lowercase w", 120: "Lowercase x",
 121: "Lowercase y", 122: "Lowercase z",
 123: "Left curly bracket", 124: "Vertical bar", 125: "Right curly bracket",
 126: "Tilde", 127: "Delete",
 128: "Euro sign", 129: "None", 130: "Single low-9 quotation mark",
 131: "Latin small letter f with hook",
 132: "Double low-9 quotation mark", 133: "Horizontal ellipsis",
 134: "Dagger", 135: "Double dagger",
 136: "Modifier letter circumflex accent", 137: "Per mille sign",
 138: "Latin capital letter S with caron",
 139: "Single left-pointing angle quotation",
 140: "Latin capital ligature OE", 141: "None",
 142: "Latin capital letter Z with caron", 143: "None",
 144: "None", 145: "Left single quotation mark",
 146: "Right single quotation mark", 147: "Left double quotation mark",
 148: "Right double quotation mark",
 149: "Bullet", 150: "En dash", 151: "Em dash", 152: "Small tilde",
 153: "Trademark sign",
 154: "Latin small letter S with caron",
 155: "Single right-pointing angle quotation mark",
 156: "Latin small ligature oe", 157: "None",
 158: "Latin small letter z with caron",
 159: "Latin capital letter Y with diaeresis",
 160: "Non-breaking space", 161: "Inverted exclamation mark",
 162: "Cent sign", 163: "Pound sign", 164: "Currency sign",
 165: "Yen sign", 166: "Pipe, broken vertical bar",
 167: "Section sign", 168: "Spacing diaeresis - umlaut",
 169: "Copyright sign", 170: "Feminine ordinal indicator",
 171: "Left double angle quotes", 172: "Not sign", 173: "Soft hyphen",
 174: "Registered trade mark sign",
 175: "Spacing macron - overline", 176: "Degree sign",
 177: "Plus-or-minus sign",
 178: "Superscript two - squared",
 179: "Superscript three - cubed", 180: "Acute accent - spacing acute",
 181: "Micro sign",
 182: "Pilcrow sign - paragraph sign", 183: "Middle dot - Georgian comma",
 184: "Spacing cedilla",
 185: "Superscript one",
 186: "Masculine ordinal indicator", 187: "Right double angle quotes",
 188: "Fraction one quarter",
 189: "Fraction one half", 190: "Fraction three quarters",
 191: "Inverted question mark", 192: "Latin capital letter A with grave",
 193: "Latin capital letter A with acute",
 194: "Latin capital letter A with circumflex",
 195: "Latin capital letter A with tilde",
 196: "Latin capital letter A with diaeresis",
 197: "Latin capital letter A with ring above",
 198: "Latin capital letter AE", 199: "Latin capital letter C with cedilla",
 200: "Latin capital letter E with grave",
 201: "Latin capital letter E with acute",
 202: "Latin capital letter E with circumflex",
 203: "Latin capital letter E with diaeresis",
 204: "Latin capital letter I with grave",
 205: "Latin capital letter I with acute",
 206: "Latin capital letter I with circumflex",
 207: "Latin capital letter I with diaeresis",
 208: "Latin capital letter ETH",
 209: "Latin capital letter N with tilde",
 210: "Latin capital letter O with grave",
 211: "Latin capital letter O with acute",
 212: "Latin capital letter O with circumflex",
 213: "Latin capital letter O with tilde",
 214: "Latin capital letter O with diaeresis",
 215: "Multiplication sign",
 216: "Latin capital letter O with slash",
 217: "Latin capital letter U with grave",
 218: "Latin capital letter U with acute",
 219: "Latin capital letter U with circumflex",
 220: "Latin capital letter U with diaeresis",
 221: "Latin capital letter Y with acute",
 222: "Latin capital letter THORN",
 223: "Latin small letter sharp s - ess-zed",
 224: "Latin small letter a with grave",
 225: "Latin small letter a with acute",
 226: "Latin small letter a with circumflex",
 227: "Latin small letter a with tilde",
 228: "Latin small letter a with diaeresis",
 229: "Latin small letter a with ring above",
 230: "Latin small letter ae",
 231: "Latin small letter c with cedilla",
 232: "Latin small letter e with grave",
 233: "Latin small letter e with acute",
 234: "Latin small letter e with circumflex",
 235: "Latin small letter e with diaeresis",
 236: "Latin small letter i with grave",
 237: "Latin small letter i with acute",
 238: "Latin small letter i with circumflex",
 239: "Latin small letter i with diaeresis",
 240: "Latin small letter eth",
 241: "Latin small letter n with tilde",
 242: "Latin small letter o with grave",
 243: "Latin small letter o with acute",
 244: "Latin small letter o with circumflex",
 245: "Latin small letter o with tilde",
 246: "Latin small letter o with diaeresis",
 247: "Division sign", 248: "Latin small letter o with slash",
 249: "Latin small letter u with grave",
 250: "Latin small letter u with acute",
 251: "Latin small letter u with circumflex",
 252: "Latin small letter u with diaeresis",
 253: "Latin small letter y with acute",
 254: "Latin small letter thorn", 255: "Latin small letter y with diaeresis "
}
## Decimal to Hexadecimal
POOL_DICTIONARY_DECIMAL_TO_HEX = {
 0: "00", 1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06",
 7: "07", 8: "08", 9: "09",
 10: "0A", 11: "0B", 12: "0C", 13: "0D", 14: "0E", 15: "0F", 16: "10",
 17: "11", 18: "12", 19: "13",
 20: "14", 21: "15", 22: "16", 23: "17", 24: "18", 25: "19", 26: "1A",
 27: "1B", 28: "1C", 29: "1D",
 30: "1E", 31: "1F", 32: "20", 33: "21", 34: "22", 35: "23", 36: "24",
 37: "25", 38: "26", 39: "27",
 40: "28", 41: "29", 42: "2A", 43: "2B", 44: "2C", 45: "2D", 46: "2E",
 47: "2F", 48: "30", 49: "31",
 50: "32", 51: "33", 52: "34", 53: "35", 54: "36", 55: "37", 56: "38",
 57: "39", 58: "3A", 59: "3B",
 60: "3C", 61: "3D", 62: "3E", 63: "3F", 64: "40", 65: "41", 66: "42",
 67: "43", 68: "44", 69: "45",
 70: "46", 71: "47", 72: "48", 73: "49", 74: "4A", 75: "4B", 76: "4C",
 77: "4D", 78: "4E", 79: "4F",
 80: "50", 81: "51", 82: "52", 83: "53", 84: "54", 85: "55", 86: "56",
 87: "57", 88: "58", 89: "59",
 90: "5A", 91: "5B", 92: "5C", 93: "5D", 94: "5E", 95: "5F", 96: "60",
 97: "61", 98: "62", 99: "63",
 100: "64", 101: "65", 102: "66", 103: "67", 104: "68", 105: "69",
 106: "6A", 107: "6B", 108: "6C", 109: "6D",
 110: "6E", 111: "6F", 112: "70", 113: "71", 114: "72", 115: "73",
 116: "74", 117: "75", 118: "76", 119: "77",
 120: "78", 121: "79", 122: "7A", 123: "7B", 124: "7C", 125: "7D",
 126: "7E", 127: "7F", 128: "80", 129: "81",
 130: "82", 131: "83", 132: "84", 133: "85", 134: "86", 135: "87",
 136: "88", 137: "89", 138: "8A", 139: "8B",
 140: "8C", 141: "8D", 142: "8E", 143: "8F", 144: "90", 145: "91",
 146: "92", 147: "93", 148: "94", 149: "95",
 150: "96", 151: "97", 152: "98", 153: "99", 154: "9A", 155: "9B",
 156: "9C", 157: "9D", 158: "9E", 159: "9F",
 160: "A0", 161: "A1", 162: "A2", 163: "A3", 164: "A4", 165: "A5",
 166: "A6", 167: "A7", 168: "A8", 169: "A9",
 170: "AA", 171: "AB", 172: "AC", 173: "AD", 174: "AE", 175: "AF",
 176: "B0", 177: "B1", 178: "B2", 179: "B3",
 180: "B4", 181: "B5", 182: "B6", 183: "B7", 184: "B8", 185: "B9",
 186: "BA", 187: "BB", 188: "BC", 189: "BD",
 190: "BE", 191: "BF", 192: "C0", 193: "C1", 194: "C2", 195: "C3",
 196: "C4", 197: "C5", 198: "C6", 199: "C7",
 200: "C8", 201: "C9", 202: "CA", 203: "CB", 204: "CC", 205: "CD",
 206: "CE", 207: "CF", 208: "D0", 209: "D1",
 210: "D2", 211: "D3", 212: "D4", 213: "D5", 214: "D6", 215: "D7",
 216: "D8", 217: "D9", 218: "DA", 219: "DB",
 220: "DC", 221: "DD", 222: "DE", 223: "DF", 224: "E0", 225: "E1",
 226: "E2", 227: "E3", 228: "E4", 229: "E5",
 230: "E6", 231: "E7", 232: "E8", 233: "E9", 234: "EA", 235: "EB",
 236: "EC", 237: "ED", 238: "EE", 239: "EF",
 240: "F0", 241: "F1", 242: "F2", 243: "F3", 244: "F4", 245: "F5",
 246: "F6", 247: "F7", 248: "F8", 249: "F9",
 250: "FA", 251: "FB", 252: "FC", 253: "FD", 254: "FE", 255: "FF"
}
## 8-bit color encodings
## Available schemes:
## descriptive-name, Binary RGB, Octal RGB, Decimal RGB, Hex RGB, RGB%,
## CMYK%, RGB, HSL< HSV, CMYK, XYZ, Yxy, Hunter Lab, CIE-Lab
## Base: 3-bit HEX,  descriptive-name, binR, binG, binB, OctalR,
## OctalG, OctalB, DecimalR, DecimalG, DecimalB, HexR, HexG, HexB,
## R%, G%, B%, C%, M%, Y%, K%, R, B, G, #H, S, L,
## H, S, V, C, M, Y, K, X, Y, Z, Y, x, y, HLR, HLG, HLB, CLR, CLG, CLB
POOL_DICTIONARY_3BIT_HEX_TRANSLATION = {
 0: ["000000", "black",           "00000000", "00000000", "00000000",
  0,        0,      0,      0,      0,      0,      '00',   '00',   '00',
  float(0.0000),   float(0.0000),   float(0.0000),   float(0.0000),
  float(0.0000),   float(0.0000),    float(100.00), 0,   0,   0],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,
  #float(0.00), float(0.00), float(0.00), float(1.00), float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000),   float(0.0000),
  #float(0.0000), float(0.0000),    float(0.0000),   float(0.0000),
  #float(0.0000), float(0.0000), float(0.0000)],
 1: ["FF00FF", "magenta",         "11111111", "00000000", "11111111",
  377,      0,      377,    1,      0,      1,      'FF',   '00',   'FF',
  float(50.0000),  float(0.0000),   float(50.0000),  float(0.0000),
  float(100.0000), float(0.0000),    float(0.0000), 255, 0,   255],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,   float(0.00),
  #float(0.00), float(0.00), float(0.00), float(0.0000),   float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000),    float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000), float(0.0000)], # not done
 2: ["0000FF", "blue",            "00000000", "00000000", "11111111",
  0,        0,      377,    0,      0,      1,      '00',   '00',   'FF',
  float(0.0000),   float(0.0000),   float(100.0000), float(100.0000),
  float(100.0000), float(0.0000),    float(0.0000), 0,   255, 0],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,   float(0.00),
  #float(0.00), float(0.00), float(0.00), float(0.0000),   float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000),    float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000), float(0.0000)], # not done
 3: ["00FFFF", "cyan",            "00000000", "11111111", "11111111",
  0,        377,    377,    0,      1,      1,      '00',   'FF',   'FF',
  float(0.0000),   float(50.0000),  float(50.0000),  float(100.0000),
  float(0.0000),   float(0.0000),    float(0.0000), 0,   255, 255],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,   float(0.00),
  #float(0.00), float(0.00), float(0.00), float(0.0000),   float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000),    float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000), float(0.0000)], # not done
 4: ["00FF00", "green",           "00000000", "11111111", "00000000",
  0,        377,    0,      0,      1,      0,      '00',   'FF',   '00',
  float(0.0000),   float(100.0000), float(0.0000),   float(1000.0000),
  float(0.0000),   float(100.0000),  float(0.0000), 0,   0,   255],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,   float(0.00),
  #float(0.00), float(0.00), float(0.00), float(0.0000),   float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000),    float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000), float(0.0000)], # not done
 5: ["FFFF00", "yellow",          "11111111", "11111111", "00000000",
  377,      377,    0,      1,      1,      0,      'FF',   'FF',   '00',
  float(50.0000),  float(50.0000),  float(0.0000),   float(0.0000),
  float(0.0000),   float(1000.0000), float(0.0000), 255, 0,   255],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,   float(0.00),
  #float(0.00), float(0.00), float(0.00), float(0.0000),   float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000),    float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000), float(0.0000)], # not done
 6: ["FF0000", "red",             "11111111", "00000000", "00000000",
  377,      0,      0,      0,      0,      1,      'FF',   '00',   '00',
  float(100.0000), float(0.0000),   float(0.0000),   float(0.0000),
  float(100.0000), float(100.0000),  float(0.0000), 255, 0,   0],
  #float(0.00), float(0.00), float(0.00), 0,   0,   0,   float(0.00)
  #float(0.00), float(0.00), float(0.00), float(0.0000),   float(0.0000),
  #float(0.0000),   float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000),    float(0.0000),   float(0.0000), float(0.0000),
  #float(0.0000), float(0.0000)], # not done
 7: ["FFFFFF", "white",           "11111111", "11111111", "11111111",
  377,      377,    377,    1,      1,      1,      'FF',   'FF',   'FF',
  float(33.330),   float(33.330),   float(33.330),   float(0.0000),
  float(0.0000),   float(0.0000),    float(0.0000), 255, 255, 255]
  #float(0.00), float(0.00), float(1.00), 0,   0,   100, float(0.00),
  #float(0.00), float(0.00), float(0.00), float(95.0500),  float(100.0000)
  #float(108.9000), float(100.0000), float(0.3127), float(-0.0104),
  #float(100.0000), float(-5.33588), float(5.4332), float(100.0000),
  #float(0.0053), float(-0.0104)]
}
## Decimal to HTML: character
POOL_DICTIONARY_DECIMAL_TO_HTML_NUMBER = {
 0: "&#0;", 1: "&#1;", 2: "&#2;", 3: "&#3;", 4: "&#4;", 5: "&#5;", 6: "&#6;",
 7: "&#7;", 8: "&#8;", 9: "&#9;", 10: "&#10;",
 11: "&#11;", 12: "&#12;", 13: "&#13;", 14: "&#14;", 15: "&#15;", 16: "&#16;",
 17: "&#17;", 18: "&#18;", 19: "&#19;", 20: "&#20;",
 21: "&#21;", 22: "&#22;", 23: "&#23;", 24: "&#24;", 25: "&#25;", 26: "&#26;",
 27: "&#27;", 28: "&#28;", 29: "&#29;", 30: "&#30;",
 31: "&#31;", 32: "&#32;", 33: "&#33;", 34: "&#34;", 35: "&#35;", 36: "&#36;",
 37: "&#37;", 38: "&#38;", 39: "&#39;", 40: "&#40;",
 41: "&#41;", 42: "&#42;", 43: "&#43;", 44: "&#44;", 45: "&#45;", 46: "&#46;",
 47: "&#47;", 48: "&#48;", 49: "&#49;", 50: "&#50;",
 51: "&#51;", 52: "&#52;", 53: "&#53;", 54: "&#54;", 55: "&#55;", 56: "&#56;",
 57: "&#57;", 58: "&#58;", 59: "&#59;", 60: "&#60;",
 61: "&#61;", 62: "&#62;", 63: "&#63;", 64: "&#64;", 65: "&#65;", 66: "&#66;",
 67: "&#67;", 68: "&#68;", 69: "&#69;", 70: "&#70;",
 71: "&#71;", 72: "&#72;", 73: "&#73;", 74: "&#74;", 75: "&#75;", 76: "&#76;",
 77: "&#77;", 78: "&#78;", 79: "&#79;", 80: "&#80;",
 81: "&#81;", 82: "&#82;", 83: "&#83;", 84: "&#84;", 85: "&#85;", 86: "&#86;",
 87: "&#87;", 88: "&#88;", 89: "&#89;", 90: "&#90;",
 91: "&#91;", 92: "&#92;", 93: "&#93;", 94: "&#94;", 95: "&#95;", 96: "&#96;",
 97: "&#97;", 98: "&#98;", 99: "&#99;", 100: "&#100;",
 101: "&#101;", 102: "&#102;", 103: "&#103;", 104: "&#104;", 105: "&#105;",
 106: "&#106;", 107: "&#107;", 108: "&#108;",
 109: "&#109;", 110: "&#110;", 111: "&#111;", 112: "&#112;", 113: "&#113;",
 114: "&#114;", 115: "&#115;", 116: "&#116;",
 117: "&#117;", 118: "&#118;", 119: "&#119;", 120: "&#120;", 121: "&#121;",
 122: "&#122;", 123: "&#123;", 124: "&#124;",
 125: "&#125;", 126: "&#126;", 127: "&#127;", 128: "&#128;", 129: "None",
 130: "&#130;", 131: "&#131;", 132: "&#132;",
 133: "&#133;", 134: "&#134;", 135: "&#135;", 136: "&#136;", 137: "&#137;",
 138: "&#138;", 139: "&#139;", 140: "&#140;",
 141: "None", 142: "&#142;", 143: "None", 144: "None", 145: "&#145;",
 146: "&#146;", 147: "&#147;", 148: "&#148;", 149: "&#149;",
 150: "&#150;", 151: "&#151;", 152: "&#152;", 153: "&#153;", 154: "&#154;",
 155: "&#155;", 156: "&#156;", 157: "None",
 158: "&#158;", 159: "&#159;", 160: "&#160;", 161: "&#161;", 162: "&#162;",
 163: "&#163;", 164: "&#164;", 165: "&#165;",
 166: "&#166;", 167: "&#167;", 168: "&#168;", 169: "&#169;", 170: "&#170;",
 171: "&#171;", 172: "&#172;", 173: "&#173;",
 174: "&#174;", 175: "&#175;", 176: "&#176;", 177: "&#177;", 178: "&#178;",
 179: "&#179;", 180: "&#180;", 181: "&#181;",
 182: "&#182;", 183: "&#183;", 184: "&#184;", 185: "&#185;", 186: "&#186;",
 187: "&#187;", 188: "&#188;", 189: "&#189;",
 190: "&#190;", 191: "&#191;", 192: "&#192;", 193: "&#193;", 194: "&#194;",
 195: "&#195;", 196: "&#196;", 197: "&#197;",
 198: "&#198;", 199: "&#199;", 200: "&#200;", 201: "&#201;", 202: "&#202;",
 203: "&#203;", 204: "&#204;", 205: "&#205;",
 206: "&#206;", 207: "&#207;", 208: "&#208;", 209: "&#209;", 210: "&#210;",
 211: "&#211;", 212: "&#212;", 213: "&#213;",
 214: "&#214;", 215: "&#215;", 216: "&#216;", 217: "&#217;", 218: "&#218;",
 219: "&#219;", 220: "&#220;", 221: "&#221;",
 222: "&#222;", 223: "&#223;", 224: "&#224;", 225: "&#225;", 226: "&#226;",
 227: "&#227;", 228: "&#228;", 229: "&#229;",
 230: "&#230;", 231: "&#231;", 232: "&#232;", 233: "&#233;", 234: "&#234;",
 235: "&#235;", 236: "&#236;", 237: "&#237;",
 238: "&#238;", 239: "&#239;", 240: "&#240;", 241: "&#241;", 242: "&#242;",
 243: "&#243;", 244: "&#244;", 245: "&#245;",
 246: "&#246;", 247: "&#247;", 248: "&#248;", 249: "&#249;", 250: "&#250;",
 251: "&#251;", 252: "&#252;", 253: "&#253;",
 254: "&#254;", 255: "&#255; "
}
## Decimal to HTML: verbose
POOL_DICTIONARY_DECIMAL_TO_HTML_NAME = {
 0: "None", 1: "None", 2: "None", 3: "None", 4: "None", 5: "None",
 6: "None", 7: "None", 8: "None", 9: "None", 10: "None",
 11: "None", 12: "None", 13: "None", 14: "None", 15: "None", 16: "None",
 17: "None", 18: "None", 19: "None", 20: "None",
 21: "None", 22: "None", 23: "None", 24: "None", 25: "None",
 26: "None", 27: "None", 28: "None",
 29: "None", 30: "None", 31: "None", 32: "None", 33: "None",
 34: "&quot;", 35: "None", 36: "None", 37: "None",
 38: "&amp;", 39: "None", 40: "None", 41: "None", 42: "None",
 43: "None", 44: "None", 45: "None",
 46: "None", 47: "None", 48: "None", 49: "None", 50: "None",
 51: "None", 52: "None", 53: "None", 54: "None", 55: "None",
 56: "None", 57: "None", 58: "None",
 59: "None", 60: "&lt;",  61: "None", 62: "&gt;", 63: "None",
 64: "None", 65: "None", 66: "None",
 67: "None", 68: "None", 69: "None", 70: "None",
 71: "None", 72: "None", 73: "None", 74: "None", 75: "None",
 76: "None", 77: "None", 78: "None",
 79: "None", 80: "None", 81: "None", 82: "None", 83: "None",
 84: "None", 85: "None", 86: "None", 87: "None",
 88: "None", 89: "None", 90: "None", 91: "None", 92: "None",
 93: "None", 94: "None", 95: "None", 96: "None",
 97: "None", 98: "None", 99: "None", 100: "None", 101: "None",
 102: "None", 103: "None", 104: "None",
 105: "None", 106: "None", 107: "None", 108: "None", 109: "None",
 110: "None", 111: "None", 112: "None", 113: "None", 114: "None", 115: "None",
 116: "None", 117: "None", 118: "None",
 119: "None", 120: "None", 121: "None", 122: "None", 123: "None",
 124: "None", 125: "None", 126: "None", 127: "None",
 128: "&euro;", 129: "None", 130: "&sbquo;", 131: "&fnof;",
 132: "&bdquo;", 133: "&hellip;", 134: "&dagger;",
 135: "&Dagger;", 136: "&circ;", 137: "&permil;", 138: "&Scaron;",
 139: "&lsaquo;", 140: "&OElig;", 141: "None",
 142: "None", 143: "None", 144: "None", 145: "&lsquo;", 146: "&rsquo;",
 147: "&ldquo;", 148: "&rdquo;", 149: "&bull;",
 150: "&ndash;", 151: "&mdash;", 152: "&tilde;", 153: "&trade;",
 154: "&scaron;", 155: "&rsaquo;", 156: "&oelig;",
 157: "None", 158: "None", 159: "&Yuml;", 160: "&nbsp;",
 161: "&iexcl;", 162: "&cent;", 163: "&pound;", 164: "&curren;",
 165: "&yen;", 166: "&brvbar;", 167: "&sect;", 168: "&uml;", 169: "&copy;",
 170: "&ordf;", 171: "&laquo;", 172: "&not;",
 173: "&shy;", 174: "&reg;", 175: "&macr;", 176: "&deg;", 177: "&plusmn;",
 178: "&sup2;", 179: "&sup3;", 180: "&acute;",
 181: "&micro;", 182: "&para;", 183: "&middot;",
 184: "&cedil;", 185: "&sup1;",
 186: "&ordm;", 187: "&raquo;", 188: "&frac14;",
 189: "&frac12;", 190: "&frac34;", 191: "&iquest;",
 192: "&Agrave;", 193: "&Aacute;",
 194: "&Acirc;", 195: "&Atilde;", 196: "&Auml;",
 197: "&Aring;", 198: "&AElig;", 199: "&Ccedil;",
 200: "&Egrave;", 201: "&Eacute;",
 202: "&Ecirc;", 203: "&Euml;", 204: "&Igrave;",
 205: "&Iacute;", 206: "&Icirc;", 207: "&Iuml;",
 208: "&ETH;", 209: "&Ntilde;",
 210: "&Ograve;", 211: "&Oacute;", 212: "&Ocirc;",
 213: "&Otilde;", 214: "&Ouml;", 215: "&times;",
 216: "&Oslash;", 217: "&Ugrave;",
 218: "&Uacute;", 219: "&Ucirc;", 220: "&Uuml;",
 221: "&Yacute;", 222: "&THORN;", 223: "&szlig;",
 224: "&agrave;", 225: "&aacute;",
 226: "&acirc;", 227: "&atilde;", 228: "&auml;",
 229: "&aring;", 230: "&aelig;", 231: "&ccedil;",
 232: "&egrave;", 233: "&eacute;",
 234: "&ecirc;", 235: "&euml;", 236: "&igrave;",
 237: "&iacute;", 238: "&icirc;", 239: "&iuml;",
 240: "&eth;", 241: "&ntilde;",
 242: "&ograve;", 243: "&oacute;", 244: "&ocirc;",
 245: "&otilde;", 246: "&ouml;", 247: "&divide;",
 248: "&oslash;", 249: "&ugrave;",
 250: "&uacute;", 251: "&ucirc;",
 252: "&uuml;", 253: "&yacute;", 254: "&thorn;", 255: "&yuml; "
}

