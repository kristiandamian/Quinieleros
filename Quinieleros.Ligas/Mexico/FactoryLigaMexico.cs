using System;

namespace Quinieleros.Ligas
{
	public static class FactoryLigaMexico
	{
		public static LigaBase GeneroLigaMexico()
		{
			LigaMexico liga = new LigaMexico ();

			return liga;	
		}
	}
}

