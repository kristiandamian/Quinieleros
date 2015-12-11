using System;
using System.Collections.Generic;

namespace Quinieleros.Ligas
{
	public abstract class EquipoBase 
	{
		public const string PrefijoIconAndroid = "@drawable/";
		public const string PrefijoIconiOS = "@drawable/";
		public string Nombre { get; set; }
		public List<string> Apodos { get; set; }

		protected string _icon;
		public string Icon { 
			get{ 
				#if __IOS__
				return string.Format ("{0}{1}", PrefijoIconiOS, _icon);
				#endif
				#if __ANDROID__
				return string.Format ("{0}{1}", PrefijoIconAndroid, _icon);
				#endif
				return string.Empty;//4 compilation baby!
			} 
			set{ 
				_icon = value;
			} 
		}
	}
}

